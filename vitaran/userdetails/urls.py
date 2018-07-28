from django.urls import path

from . import views

app_name = 'urldetails'
urlpatterns = [
    path('', views.userdetail, name='userdetail'),
    path('', views.adddetails, name='adddetails'),
]