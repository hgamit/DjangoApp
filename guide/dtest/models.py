from django.db import models
from django.contrib.auth.models import User
from delivery.models import UserAddress


class TestPackage(models.Model):
    customer = models.ForeignKey(User, related_name='testpackage', on_delete=models.DO_NOTHING)
    package_description = models.CharField(max_length = 255)
    package_descriptionhid = models.CharField(max_length = 255)
    package_descriptionplus = models.CharField(max_length = 255)

class Package(models.Model):

    FOOD = 'Food'
    GROCERY = 'Grocery'
    DOCS = 'Documents'
    HUMANWEAR = 'Humanwear'
    HOMEWEAR = 'Homewear'
    HEALTH = 'Health'
    MEDICINE = 'Medicine'
    ELECTRONICS = 'Electronics'

    PACKAGE_TYPE = (
        (FOOD, 'Food'),
        (GROCERY, 'Grocery'),
        (DOCS, 'Documents'),
        (HUMANWEAR, 'Humanwear'),
        (HOMEWEAR, 'Homewear'),
        (HEALTH, 'Health'),
        (MEDICINE, 'Medicine'),
        (ELECTRONICS, 'Electronics'),
    )

    IMMEDIATE = 'Within 2 Hours'
    FOURHOURS = 'Within 4 Hours'
    SAMEDAY = 'Same day Delivery(24x1)'
    THREEDAYS = 'Three day Delivery(24x3)'
    WEEK = 'Within a Week(24x7)'
    TWOWEEK = 'Within Two Weeks'
    MONTH = 'Within a Month'
    THREEMONTHS = 'Within Three Months'
    SIXMONTHS = 'Within Six Months'

    DELIVERY_TIME = (
        (IMMEDIATE, 'Within 2 Hours'),
        (FOURHOURS, 'Within 4 Hours'),
        (SAMEDAY, 'Same day Delivery(24x1)'),
        (THREEDAYS, 'Three day Delivery(24x3)'),
        (WEEK, 'Within a Week(24x7)'),
        (TWOWEEK, 'Within Two Weeks'),
        (MONTH, 'Within a Month'),
        (THREEMONTHS, 'Within Three Months'),
        (SIXMONTHS, 'Within Six Months'),
    )

    SMALL = 'Small (Under 15 x 12 x 1)'
    MEDIUM = 'Medium (Under 15 x 12 x 6)'
    LARGE = 'Large (Under 24 x 12 x 6)'
 
    PACKAGE_DIM = (
        (SMALL, 'Small (Under 15 x 12 x 1)'),
        (MEDIUM, 'Medium (Under 15 x 12 x 6)'),
        (LARGE, 'Large (Under 24 x 12 x 6)'),
    )


    customer = models.ForeignKey(User, related_name='upackage', on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True) #Adds current Date and Time
    pickup_adrs = models.ForeignKey(UserAddress, related_name='+', on_delete=models.DO_NOTHING)
    delivery_adrs = models.ForeignKey(UserAddress, related_name='+', on_delete=models.DO_NOTHING)
    package_type = models.CharField(max_length=50, choices = PACKAGE_TYPE) 
    package_description = models.CharField(max_length = 255)
    package_weight = models.DecimalField(max_digits=10, decimal_places=3)
    package_dimensions = models.CharField(max_length = 255, choices = PACKAGE_DIM)
    package_value = models.CharField(max_length = 255)
    delivery_timeline = models.CharField(max_length=50, choices = DELIVERY_TIME) 
    driving_distance = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    bicycling_distance = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    transit_distance = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    driving_duration = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    bicycling_duration = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    transit_duration = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    shipping_charge = models.CharField(max_length = 255, default = "5")
    payment_status = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.customer.username

