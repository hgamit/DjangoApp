from django.shortcuts import render, redirect, get_object_or_404
from dmanage.models import UserPackage
from django.views.generic import UpdateView, DetailView, FormView, ListView, DeleteView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dmanage.forms import UserPackageForm
from django.urls import reverse_lazy
from delivery.models import UserAddress
from django.conf import settings

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
