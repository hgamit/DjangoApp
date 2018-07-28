from django.urls import path

from . import views

app_name = 'delivery'
urlpatterns = [
    path('getdetails/', views.getdetails, name='getdetails'),
    path('showdetails/', views.user_details, name='showdetails'),
    path('fileupload/', views.model_form_upload, name='fileupload'),
    path('updatedetails/', views.UserUpdateDetail.as_view(), name='updatedetails'),
]