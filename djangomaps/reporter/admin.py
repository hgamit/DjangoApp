from django.contrib import admin
from .models import Incidences, Countie
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
        list_display = ('name', 'location')

admin.site.register(Incidences, IncidencesAdmin)

class CountieAdmin(LeafletGeoAdmin):
        list_display = ('counties', 'codes')

admin.site.register(Countie, CountieAdmin)