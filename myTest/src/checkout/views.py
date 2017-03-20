from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
	
@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id
	if request.method == 'POST':
		token = request.POST['stripeToken']
		#Create a Charge : this will charge user's card
		try:
			customer = stripe.Customer.retrieve(customer_id)
			customer.sources.create(source=token)
			charge = stripe.Charge.create(
				amount=1000, #in cents
				currency="usd",
			    customer=customer,
				description="Example Charge"
			)
		except stripe.error.CardError as e:
		#Declined
			pass
	context = {'publishKey':publishKey}
	template = 'checkout.html'
	return render(request,template,context)