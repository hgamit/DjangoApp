from urllib import error

from django.contrib.gis import geos
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from geopy.geocoders.googlev3 import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError

from .models import Shop
from nearby import forms
from nearby import models


def geocode_address(address):
    address = address.encode('utf-8')
    geocoder = GoogleV3()
    try:
        _, latlon = geocoder.geocode(address)
    except (error.URLError, GeocoderQueryError, ValueError):
        return None
    else:
        return latlon

def get_shops(longitude, latitude):
    current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude))
    distance_from_point = {'km': 100000}
    #shops = Shop.objects.filter(location__distance_lte=(current_point, Distance(**distance_from_point)))
    #shops = shops.Distance(current_point).order_by('Distance')
    shops = Shop.objects.filter(location__distance_lte=(current_point, D(**distance_from_point) )).annotate(distance=(Distance('location', current_point)/1609.34)).order_by('distance')
    return shops

def home(request):
    form = forms.AddressForm()
    shops = []
    if request.POST:
        form = forms.AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            location = geocode_address(address)
            if location:
                latitude, longitude = location
                shops = get_shops(longitude, latitude)

    return render(request, 'nearby/home.html', context = {'form': form, 'shops': shops})