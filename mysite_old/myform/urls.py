from django.conf.urls import url

from . import views

app_name = 'myform'

urlpatterns = [
    url(r'^$', views.manage_authors, name='manage_authors'),

]