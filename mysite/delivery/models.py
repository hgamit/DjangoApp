from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return "%s/%s" %(instance.customer.username, filename)

class Document(models.Model):
    customer = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UserDetail(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    TRANS = 'Trans'
    SEX_TYPE = (
        (MALE,'Male'),
        (FEMALE,'Female'),
        (TRANS,'Transgender'),
    )

    customer = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_pic = models.FileField(upload_to=user_directory_path, default='image.jpg')
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please make sure phone number format: '+199999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list    
    sex = models.CharField(max_length = 11, choices = SEX_TYPE)
    date_of_birth = models.DateField(max_length=8)
    all_given = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True) #Adds current Date and Time
    # ssn_regex = RegexValidator(regex=r"^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$", message="Please enter vallid Social Security Number")
    # ssn_number = models.CharField(validators=[ssn_regex], max_length=11) # validators should be a list        
    # num_delivery_created = models.IntegerField(default=0)
    # num_delivery_made = models.IntegerField(default=0)
    # rank = models.IntegerField(default=0)
    # balance = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)    
    # dl_state = models.CharField(max_length = 2)
    # dl_number = models.CharField(max_length=11) # validators should be a list

    def __str__(self):
        return self.customer.username

class CreateDelivery(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    pickup_adrs = models.CharField(max_length=100)
    delivery_adrs = models.CharField(max_length=100)
    delivery_distance = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    expected_deliveryby = models.DateTimeField()
    package_label = models.CharField(max_length=100) 
    package_type = models.CharField(max_length=100)
    package_desc = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='deliveries', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.package_label


class MakeDelivery(models.Model):
    pickuprequested_at = models.DateTimeField(auto_now_add=True)
    pickupaccespted_at = models.DateTimeField(auto_now_add=True)
    picked_at = models.DateTimeField(auto_now_add=True)
    estimated_deliverytime = models.DateTimeField()
    delivery_num = models.ForeignKey(CreateDelivery, on_delete=models.DO_NOTHING)
    current_status = models.CharField(max_length=100)
    requested_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.delivery_num