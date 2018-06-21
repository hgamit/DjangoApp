from django.urls import path

from . import views

app_name = 'reporter'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('county_data/', views.county_datasets, name='county'),
    path('incidences_data/', views.incidences_datasets, name='incidences'),
]