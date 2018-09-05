from django.urls import path
from . import views

app_name = 'delivery'
urlpatterns = [
    path('new_userdetail/', views.new_userdetail, name='new_userdetail'),
    path('display_userdetail/', views.UserDetailDisplay.as_view(), name='display_userdetail'),
    path('edit_userdetail/', views.UserDetailUpdateView.as_view(), name='edit_userdetail'),
    path('new_securityinfo/', views.new_securityinfo, name='new_securityinfo'),
    path('display_securityinfo/', views.UserSecurityInfoDisplay.as_view(), name='display_securityinfo'),
    path('edit_securityinfo/', views.UserSecurityInfoUpdateView.as_view(), name='edit_securityinfo'),
    path('new_useraddress/', views.UserAddressCreateView.as_view(), name='new_useraddress'),
    path('display_useraddress/', views.UserAddressDisplay.as_view(), name='display_useraddress'),
    path('<address_pk>/edit_useraddress/', views.UserAddressUpdateView.as_view(), name='edit_useraddress'),
    path('<address_pk>/delete_useraddress/', views.UserAddressDeleteView.as_view(), name='delete_useraddress'),
]
