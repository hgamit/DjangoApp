from django.forms import ModelForm
from userdetails.models import UserDetail


class SignupForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = ['first_name', 'last_name', 'phone_number','sex']

    # A custom method required to work with django-allauth, see https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Save your profile
        profile = UserDetail()
        profile.user = user
        profile.phone_number = self.cleaned_data['phone_number']
        profile.sex = self.cleaned_data['sex']
        profile.save()