from django import forms
from dmanage.models import UserPackage, UserBilling
from django.utils.translation import ugettext_lazy as _

class UserPackageForm(forms.ModelForm):
    class Meta:
        model = UserPackage
        fields = (
            "pickup_adrs",
            "delivery_adrs",
            "package_type", 
            "package_description", 
            "package_weight", 
            "package_dimensions", 
            "package_value", 
            "delivery_timeline", 
            "driving_distance", 
            "bicycling_distance", 
            "transit_distance", 
            "driving_duration", 
            "bicycling_duration", 
            "transit_duration")
        widgets={
            "package_description":forms.TextInput(attrs={'placeholder':'It contains fragile item.'}),
            "package_weight":forms.NumberInput(attrs={'placeholder':'Approx. weight below 30 pounds', 'min' : '0'}),  
            "package_value":forms.NumberInput(attrs={'placeholder':'Below $5000', 'min' : '0'}),
            "driving_distance":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "bicycling_distance":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "transit_distance":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "driving_duration":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "bicycling_duration":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            "transit_duration":forms.NumberInput(attrs={'type':'hidden', 'min' : '0'}),
            }


"""
Add a simple form, which includes the hidden payment nonce field.

You might want to add other fields like an address, quantity or
an amount.

"""

class CheckoutForm(forms.ModelForm):
    payment_method_nonce = forms.CharField(
        max_length=1000,
        widget=forms.widgets.HiddenInput,
        #require=False,  # In the end it's a required field, but I wanted to provide a custom exception message
    )
    class Meta:
        model = UserBilling
        fields = (
             "billing_adrs",
         )
    
    def clean(self):
        self.cleaned_data = super(CheckoutForm, self).clean()
        # Braintree nonce is missing
        if not self.cleaned_data.get('payment_method_nonce'):
            raise forms.ValidationError(_(
                'We couldn\'t verify your payment. Please try again.'))
        return self.cleaned_data