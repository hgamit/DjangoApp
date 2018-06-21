from django.contrib import admin
from .models import Shop
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget


class ShopAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
admin.site.register(Shop, ShopAdmin)
