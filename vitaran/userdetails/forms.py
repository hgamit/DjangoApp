from django.forms import ModelForm
from userdetails.models import UserDetail
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .validators import is_corect

class UserDetailForm(ModelForm):
    class Meta:
        model = UserDetail
        exclude = ['user']

    # A custom method required to work with django-allauth, see https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
    def adddetails(self, request, user):
        # Save your profile
        profile = UserDetail()
        profile.user = user
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        #profile.phone_number = self.cleaned_data['phone_number']
        #profile.sex = self.cleaned_data['sex']
        profile.save()

    # def clean(self):
    #     cleaned_data = super(UserDetailForm, self).clean()
    #     dl_state = cleaned_data.get("dl_state")
    #     dl_number = cleaned_data.get("dl_number")
    #     if(not(is_corect(dl_number,dl_state))):
    #         raise ValidationError("Please provide valid state and licence number.")
