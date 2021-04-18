from django.db import models
from django.db.models import Func, F
from django.db.models.functions import Cast
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USSocialSecurityNumberField
from delivery.models import UserAddress

class WithDistanceManager(models.Manager):
    def with_distance(self, pickup_adrs_lat, pickup_adrs_lng):
        """
        Returns a QuerySet of locations annotated with their distance from the
        given point. This can then be filtered.
        Usage:
            Foo.objects.with_distance(lat, lon).filter(distance__lt=10).count()
        @see http://stackoverflow.com/a/31715920/1373318
        """
        class Sin(Func):
            function = 'SIN'
        class Cos(Func):
            function = 'COS'
        class Acos(Func):
            function = 'ACOS'
        class Radians(Func):
            function = 'RADIANS'           

        radlat = Radians(pickup_adrs_lat) # given latitude
        radlong = Radians(pickup_adrs_lng) # given longitude
        #lat = UserPackage.objects.select_related('pickup_adrs').values('pickup_adrs__lat')
        #lng = UserPackage.objects.select_related('pickup_adrs').values('pickup_adrs__lng')
        radflat = Radians(F('pickup_adrs_lat'))
        radflong = Radians(F('pickup_adrs_lng'))

        # Note 3959.0 is for miles. Use 6371 for kilometers
        Expression = 3959.0 * Acos(Cos(radlat) * Cos(radflat) *
                                   Cos(radflong - radlong) +
                                   Sin(radlat) * Sin(radflat))

        return self.get_queryset()\
            .annotate(distance=models.ExpressionWrapper(Cast(Expression,models.DecimalField(max_digits=10, decimal_places=2)), output_field=models.DecimalField()))


class UserPackage(models.Model):

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


    customer = models.ForeignKey(User, related_name='userpackage', on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True) #Adds current Date and Time
    pickup_adrs = models.ForeignKey(UserAddress, related_name='pickupa', on_delete=models.DO_NOTHING)
    pickup_adrs_lat = models.DecimalField(max_digits=10, decimal_places=6, default = 0.0)
    pickup_adrs_lng = models.DecimalField(max_digits=10, decimal_places=6, default = 0.0)
    delivery_adrs = models.ForeignKey(UserAddress, related_name='deliverya', on_delete=models.DO_NOTHING)
    package_type = models.CharField(max_length=50, choices = PACKAGE_TYPE) 
    package_description = models.CharField(max_length = 255)
    package_weight = models.DecimalField(max_digits=10, decimal_places=3)
    package_dimensions = models.CharField(max_length = 255, choices = PACKAGE_DIM)
    package_value = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    delivery_timeline = models.CharField(max_length=50, choices = DELIVERY_TIME) 
    driving_distance = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    bicycling_distance = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    transit_distance = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    driving_duration = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    bicycling_duration = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    transit_duration = models.DecimalField(max_digits=10, decimal_places=3, default = 0.0)
    shipping_charge = models.CharField(max_length = 255, default = "5")
    #payment_nonce = models.CharField(max_length=100,null=True,blank=True)
    txnid = models.CharField(max_length=25,null=True,blank=True)
    payment_status = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    objects = WithDistanceManager()

    def __str__(self):
        return self.customer.username


class UserBilling(models.Model):
    customer = models.OneToOneField(User, on_delete=models.DO_NOTHING,related_name='userbilling')
    #client_token = models.TextField(verbose_name=u'client token', max_length=500)
    btree_id = models.CharField(max_length=25,null=True,blank=True)
    billing_adrs = models.ForeignKey(UserAddress, related_name='billinga', on_delete=models.DO_NOTHING)
    #payment_mode = models.BooleanField(default=False)
    
    def __str__(self):
        return self.customer.username 
