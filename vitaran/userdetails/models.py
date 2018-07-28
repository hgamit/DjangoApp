import re
from django.db import models
from django.forms import ModelForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .validators import is_corect
# This model stores detailed user information.

class UserDetail(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    TRANS = 'Trans'
    SEX_TYPE = (
        (MALE,'Male'),
        (FEMALE,'Female'),
        (TRANS,'Transgender'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please make sure phone number format: '+199999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list    
    # sex = models.CharField(max_length = 5, choices = SEX_TYPE)
    # date_of_birth = models.DateField(max_length=8)
    # ssn_regex = RegexValidator(regex=r"^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$", message="Please enter vallid Social Security Number")
    # ssn_number = models.CharField(validators=[ssn_regex], max_length=11) # validators should be a list        
    # num_delivery_created = models.IntegerField(default=0)
    # num_delivery_made = models.IntegerField(default=0)
    # rank = models.IntegerField(default=0)
    # balance = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)    
    # dl_state = models.CharField(max_length = 2)
    # dl_number = models.CharField(max_length=11) # validators should be a list

    def __str__(self):
        return self.user.name

    
    
"""     def clean(self):
        cleaned_data = super(UserDetail, self).clean()
        dl_state = cleaned_data.get("dl_state")
        dl_number = cleaned_data.get("dl_number")
        if(not(is_corect(dl_number,dl_state))):
            raise ValidationError("Please provide valid state and licence number.")
 """
    
    

# class UserDetailForm(ModelForm):
#     class Meta:
#         model = UserDetail
#         exclude = ['user']