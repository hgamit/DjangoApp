from django import forms
from .models import Shop

from mapwidgets.widgets import GooglePointFieldWidget

class ShopAdminForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ("name", "location")
        widgets = {
            'name': GooglePointFieldWidget,
            'location': GooglePointFieldWidget,
        }


class AddressForm(forms.Form):
    address = forms.CharField()