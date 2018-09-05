from django.urls import path
from . import views

app_name = 'dmanage'
urlpatterns = [
    path('new_userpackage/', views.UserPackageCreateView.as_view(), name='new_userpackage'),
    path('<package_pk>/display_userpackage/', views.UserPackageDisplay.as_view(), name='display_userpackage'),
    #path('<address_pk>/edit_useraddress/', views.UserAddressUpdateView.as_view(), name='edit_useraddress'),
    #path('<address_pk>/delete_useraddress/', views.UserAddressDeleteView.as_view(), name='delete_useraddress'),
]
