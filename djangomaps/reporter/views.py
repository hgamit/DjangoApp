from django.shortcuts import render
from django.views import generic
from django.core.serializers import serialize
from .models import Countie, Incidences
from django.http import HttpResponse

# Create your views here.

class HomePageView(generic.TemplateView):
    template_name = 'index.html'

def county_datasets(request):
    counties = serialize('geojson', Countie.objects.all() )
    return HttpResponse(counties, content_type='json')

def incidences_datasets(request):
    incidences = serialize('geojson', Incidences.objects.all() )
    return HttpResponse(incidences, content_type='json')