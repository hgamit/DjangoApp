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
    path('new_address/', views.UserAddressCreateView.as_view(), name='new_address'),
    #path('display_address/<address_pk>', views.display_address, name='display_address'),
    path('display_address/', views.UserAddressDisplay.as_view(), name='display_address'),
    path('<address_pk>/edit_address/', views.UserAddressUpdateView.as_view(), name='edit_address'),
    path('<address_pk>/delete_address/', views.UserAddressDeleteView.as_view(), name='delete_address'),
]
