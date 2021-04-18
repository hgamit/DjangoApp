from django.urls import path
from . import views

app_name = 'dpickup'
urlpatterns = [
    path('packages_nearby/', views.UserSearchCreateView.as_view(), name='packages_nearby'),
    #path('packages_nearby/', views.packages_nearby, name='packages_nearby'),
    #path('packages_search/', views.packages_search, name='packages_search'),
    #path('<package_pk>/display_userpackage/', views.UserPackageDisplay.as_view(), name='display_userpackage'),
    #path('<address_pk>/edit_useraddress/', views.UserAddressUpdateView.as_view(), name='edit_useraddress'),
    #path('<address_pk>/delete_useraddress/', views.UserAddressDeleteView.as_view(), name='delete_useraddress'),
]
