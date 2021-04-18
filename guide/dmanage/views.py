from django.shortcuts import render, redirect, get_object_or_404, reverse
from dmanage.models import UserPackage, UserBilling
from django.views.generic import UpdateView, DetailView, FormView, ListView, DeleteView, CreateView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dmanage.forms import UserPackageForm, CheckoutForm
from django.urls import reverse_lazy
from delivery.models import UserAddress
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import braintree
from django.http import HttpResponse


"""
Adds simple form view, which communicates with Braintree.

There are four steps to finally process a transaction:

1. Create a client token (views.py)
2. Send it to Braintree (js)
3. Receive a payment nonce from Braintree (js)
4. Send transaction details and payment nonce to Braintree (views.py)

"""

class CheckoutView(CreateView):
    """This view lets the user initiate a payment."""
    # model = UserPackage
    form_class = CheckoutForm
    # pk_url_kwarg = 'package_pk'
    # context_object_name = 'package'
    success_url = reverse_lazy("delivery:display_useraddress")
    template_name = 'dmanage/checkout.html'

    def form_valid(self, form):
        billing_adrs = ""
        if form.is_valid():
            try:
                user = UserBilling.objects.get(customer_id=self.request.user.id)
            except UserBilling.DoesNotExist:
                # Braintree customer info. You can, for sure, use several approaches to gather customer infos
                # For now, we'll simply use the given data of the user instance
                customer_kwargs = {
                    "first_name": self.user.first_name,
                    "last_name": self.user.last_name,
                    "email": self.user.email,
                    }
                # Create a new Braintree customer
                # In this example we always create new Braintree users
                # You can store and re-use Braintree's customer IDs, if you want to
                result = braintree.Customer.create(customer_kwargs)
                if not result.is_success:
                    # Ouch, something went wrong here
                    # I recommend to send an error report to all admins
                    # , including ``result.message`` and ``self.user.email``
                    context = self.get_context_data()
                    # We re-generate the form and display the relevant braintree error
                    context.update({
                        'form': self.get_form(self.get_form_class()),
                        'braintree_error': u'{} {}'.format(
                            result.message, _('Please get in contact.'))
                            })
                    return HttpResponse("c-failed")
                    #return self.render_to_response(context)
                else:
                    # If the customer creation was successful you might want to also
                    # add the customer id to your user profile
                    checkout = form.save(commit=False)
                    checkout.customer = self.request.user
                    checkout.btree_id = result.customer.id
                    #checkout.client_token = "Ctoken"
                    billing_adrs = form.cleaned_data['billing_adrs']
                    checkout.save()

            """
            Create a new transaction and submit it.
            I don't gather the whole address in this example, but I can
            highly recommend to do that. It will help you to avoid any
            fraud issues, since some providers require matching addresses
            
            """
            upackage = UserPackage.objects.get(id=self.kwargs['package_pk'])
            user = UserBilling.objects.get(customer_id=self.request.user.id)

            if upackage:
                billing_address = {
					"first_name": self.user.first_name,
					"last_name": self.user.last_name,
					#"Address": billing_adrs,
				}
                
                shipping_address = {
					"first_name": self.user.first_name,
					"last_name": self.user.last_name,
					#"Address": upackage.delivery_adrs,
				}
				
                address_dict = {
                    "first_name": self.user.first_name,
                    "last_name": self.user.last_name,
                    "street_address": '2171 Grand Ave',
                    "extended_address": 'street_2',
                    "locality": 'St Paul',
                    "region": 'MN',
                    "postal_code": 55105,
                    #"country_code_alpha2": 'alpha2_country_code',
                    #"country_code_alpha3": 'alpha3_country_code',
                    "country_name": 'USA',
                    #"country_code_numeric": 'numeric_country_code',
                    }

				# You can use the form to calculate a total or add a static total amount
				# I'll use a static amount in this example
                result = braintree.Transaction.sale({
					"customer_id": user.btree_id,
					"amount": upackage.shipping_charge,
					"payment_method_nonce": form.cleaned_data['payment_method_nonce'],
					"descriptor": {
						# Definitely check out https://developers.braintreepayments.com/reference/general/validation-errors/all/python#descriptor
						"name": "COMPANY.*test",
					},
					"billing": address_dict,
					"shipping": address_dict,
					"options": {
						# Use this option to store the customer data, if successful
						'store_in_vault_on_success': True,
						# Use this option to directly settle the transaction
						# If you want to settle the transaction later, use ``False`` and later on
						# ``braintree.Transaction.submit_for_settlement("the_transaction_id")``
						'submit_for_settlement': True,
					},
				})
                if not result.is_success:
                    # Card could've been declined or whatever
                    # I recommend to send an error report to all admins
                    # , including ``result.message`` and ``self.user.email``
                    context = self.get_context_data()
                    context.update({
                        'form': self.get_form(self.get_form_class()),
                        'braintree_error': _(
                            'Your payment could not be processed. Please check your'
                            ' input or use another payment method and try again.')
                    })
                    return HttpResponse(form.cleaned_data['payment_method_nonce'])
                    #return self.render_to_response(context)

                else:
                    # Finally there's the transaction ID
                    # You definitely want to send it to your database
                    upackage.txnid = result.transaction.id
                    upackage.payment_status = True
                    upackage.save()
                    
                    # Now you can send out confirmation emails or update your metrics
                    # or do whatever makes you and your customers happy :)
            return super(CheckoutView, self).form_valid(form)


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # We need the user to assign the transaction
        self.user = request.user
        
        # Ha! There it is. This allows you to switch the
        # Braintree environments by changing one setting
        if settings.BRAINTREE_PRODUCTION:
            braintree_env = braintree.Environment.Production
        else:
            braintree_env = braintree.Environment.Sandbox
            
        # Configure Braintree
        braintree.Configuration.configure(
            braintree_env,
            merchant_id=settings.BRAINTREE_MERCHANT_ID,
            public_key=settings.BRAINTREE_PUBLIC_KEY,
            private_key=settings.BRAINTREE_PRIVATE_KEY,
        )
        
        # Generate a client token. We'll send this to the form to
        # finally generate the payment nonce
        # You're able to add something like ``{"customer_id": 'foo'}``,
        # if you've already saved the ID
        self.braintree_client_token = braintree.ClientToken.generate({})
        # user = get_object_or_404(UserBilling, id=request.user.id)
        # if not user.customer_id:
        #     self.braintree_client_token = braintree.ClientToken.generate({})
        # else:
        #     self.braintree_client_token = braintree.ClientToken.generate({
        #         "customer_id": user.customer_id
        #     })

        return super(CheckoutView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        ctx = super(CheckoutView, self).get_context_data(**kwargs)
        package = UserPackage.objects.get(id=self.kwargs['package_pk'])
        ctx.update({
            'braintree_client_token': self.braintree_client_token,
            'package': package,
            'u': self.request.user
        })
        return ctx
		
    def get_success_url(self):
        # Add your preferred success url
        return reverse('boards:home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(customer=self.request.user)


# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserPackageCreateView(FormView):
    template_name = "dmanage/new_userpackage.html"
    form_class = UserPackageForm
    success_url = reverse_lazy("boards:home")

    def form_valid(self, form):
        detail = form.save(commit=False)
        detail.customer = self.request.user
        driving_distance = form.cleaned_data['driving_distance']
        driving_duration = form.cleaned_data['driving_duration']
        package_dimensions = form.cleaned_data['package_dimensions']
        delivery_timeline = form.cleaned_data['delivery_timeline']
        detail.pickup_adrs_lat = form.cleaned_data['pickup_adrs'].lat
        detail.pickup_adrs_lng = form.cleaned_data['pickup_adrs'].lng
        #detail.pickup_adrs_lat = UserAddress.objects.values_list("lat", flat=True).filter(pickupa=pickup_adrs_val)

        charge = 5.0
        if driving_distance > 50 and 4<driving_duration<24 and delivery_timeline == "Same day Delivery(24x1)":
            charge += 10
        elif driving_distance > 50 and driving_duration>24:
            charge += 5
        else:
            if (package_dimensions == "Small (Under 15 x 12 x 1)" or package_dimensions == "Medium (Under 15 x 12 x 6)") and (delivery_timeline == "Within 2 Hours" or delivery_timeline == "Within 2 Hours"):
                charge += 10
            elif package_dimensions == "Large (Under 24 x 12 x 6)" and (delivery_timeline == "Within 2 Hours" or delivery_timeline == "Within 2 Hours"):
                charge += 12
            elif delivery_timeline== "Same day Delivery(24x1)":
                charge += 8
            else:
                charge += 5

        detail.shipping_charge = charge
        detail.save()

        if detail is not None:
            return redirect('dmanage:display_userpackage' , detail.id)
        else:
            return super(UserPackageCreateView, self).form_valid(form)

    def get_object(self,queryset=None):
        return self.request.user.userpackage

    def get_context_data(self, **kwargs):
        context = super(UserPackageCreateView, self).get_context_data(**kwargs)
        context['GMAPS'] = settings.GOOGLE_API_KEY
        return context

@method_decorator(login_required, name='dispatch')
class UserPackageDisplay(DetailView):
    model = UserPackage
    #queryset = UserPackage.objects.all() # querying DB
    template_name = 'dmanage/display_userpackage.html'
    pk_url_kwarg = 'package_pk'
    context_object_name = 'package'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(customer=self.request.user)
