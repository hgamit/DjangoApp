from django.db import models
from django.contrib.auth.models import User

class UserSearch(models.Model):

    customer = models.ForeignKey(User, related_name='usersearch', on_delete=models.DO_NOTHING)
    date_searched = models.DateTimeField(auto_now_add=True) #Adds current Date and Time
    search_adrs = models.CharField(max_length = 255)
    search_adrs_lat = models.DecimalField(max_digits=10, decimal_places=6, default = 0.0)
    search_adrs_lng = models.DecimalField(max_digits=10, decimal_places=6, default = 0.0)

    def __str__(self):
        return self.customer.username


