from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USSocialSecurityNumberField
#from django.contrib.gis.db import models as gis_models
#from django.contrib.gis.geos import Point


def user_directory_path(instance, filename):
    return "%s/%s" %(instance.customer.username, filename)

class UserDetail(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    TRANS = 'Trans'
    SEX_TYPE = (
        (MALE,'Male'),
        (FEMALE,'Female'),
        (TRANS,'Transgender'),
    )

    customer = models.OneToOneField(User, on_delete=models.DO_NOTHING,related_name='userprofile')
    user_pic = models.FileField(upload_to=user_directory_path, default='image.jpg')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please make sure phone number format: '+199999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list    
    sex = models.CharField(max_length = 11, choices = SEX_TYPE)
    date_of_birth = models.DateField(max_length=8)
    #all_given = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True) #Adds current Date and Time
    # ssn_regex = RegexValidator(regex=r"^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$", message="Please enter vallid Social Security Number")
    # ssn_number = models.CharField(validators=[ssn_regex], max_length=11) # validators should be a list        
    #num_delivery_created = models.IntegerField(default=0)
    #num_delivery_made = models.IntegerField(default=0)
    #rank = models.IntegerField(default=0)
    #balance = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)    
    # dl_state = models.CharField(max_length = 2)
    # dl_number = models.CharField(max_length=11) # validators should be a list

    def __str__(self):
        return self.customer.username


class UserSecurityInfo(models.Model):

    customer = models.OneToOneField(User, on_delete=models.DO_NOTHING,related_name='usersecurity')
    #ssn_regex = RegexValidator(regex=r"^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$", message="Please enter vallid Social Security Number")
    #ssn_number = models.CharField(validators=[ssn_regex], max_length=11) # validators should be a list   714-23-8324
    ssn_number = USSocialSecurityNumberField()
    ssn_img = models.ImageField(upload_to=user_directory_path, default='ssn.jpg')
    dl_state = USStateField()
    dl_number = models.CharField(max_length=13) # validators should be a list M263634281411 MN
    dlside1_img = models.ImageField(upload_to=user_directory_path, default='dlside1.jpg')
    dlside2_img = models.ImageField(upload_to=user_directory_path, default='dlside2.jpg')
    #all_given = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True) #Adds current Date and Time

    def __str__(self):
        return self.customer.username


#POINT = Point(-104.9903, 39.7392, srid=4326)

class UserAddress(models.Model):
    PERMANENT = 'Permanent'
    COMMUNICATION = 'Communication'
    RECEIVER = 'Receiver'
    ADDRESS_TYPE = (
        (PERMANENT,'Permanent'),
        (COMMUNICATION,'Communication'),
        (RECEIVER,'Receiver'),
    )


    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='uaddress')
    po_box_number = models.CharField(max_length=255)
    address_type = models.CharField(max_length = 13, choices = ADDRESS_TYPE, default="Communication")
    street_number = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    point_of_contact = models.CharField(max_length=255,default="")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please make sure phone number format: '+199999999'. Up to 15 digits allowed.")
    contact_phone = models.CharField(validators=[phone_regex], max_length=17, default="")
    ##coordinates = gis_models.PointField(help_text="To generate the map for your location")
    last_updated = models.DateTimeField(auto_now_add=True) #Adds current Date and Time

    def __str__(self):
        return self.customer.username
