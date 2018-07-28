from django import forms
from delivery.models import UserDetail, UserSecurityInfo, UserAddress
from delivery.validators import is_correct
# import GooglePointFieldWidget, GoogleStaticMapWidget, GoogleStaticOverlayMapWidget

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['user_pic', 'phone_number', 'sex', 'date_of_birth']

class UserSecurityInfoForm(forms.ModelForm):
    class Meta:
        model = UserSecurityInfo
        fields = ['ssn_number', 'ssn_img', 'dl_state', 'dl_number', 'dlside1_img', 'dlside2_img']

    def clean(self):
        cleaned_data = super().clean()
        dl_state = cleaned_data.get("dl_state")
        dl_number = cleaned_data.get("dl_number")

        if not (is_correct(dl_state,dl_number)):
            raise forms.ValidationError(
                    #is_correct(dl_state,dl_number)
                    dl_state+" "+dl_number+"Make sure you provided correct State and Identity Details."
                    #"More Description"
                )

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ("po_box_number","address_type","street_number", "route", "city", "state", "country", "zip_code", "point_of_contact", "contact_phone")
        widgets={
            "po_box_number":forms.TextInput(attrs={'placeholder':'PO Box/House/Apartment Number','id':'po_box_number'}),
            #"address_type":forms.TextInput(attrs={'placeholder':'Type of Address','id':'address_type'}),
            "street_number":forms.TextInput(attrs={'placeholder':'Street Number','id':'street_number'}),
            "route":forms.TextInput(attrs={'placeholder':'Avenue','id':'route'}),  
            "city":forms.TextInput(attrs={'placeholder':'City','id':'locality'}),
            "state":forms.TextInput(attrs={'placeholder':'State','id':'administrative_area_level_1'}),
            "country":forms.TextInput(attrs={'placeholder':'Country','id':'country'}),
            "zip_code":forms.TextInput(attrs={'placeholder':'Postal Code','id':'postal_code'}),
            "point_of_contact":forms.TextInput(attrs={'placeholder':'Residents Full Name','id':'point_of_contact'}),
            "contact_phone":forms.TextInput(attrs={'placeholder':'Residents Phone','id':'contact_phone'}),
            #"coordinates":forms.Textarea(attrs={'id':'coordinates'}),
            }