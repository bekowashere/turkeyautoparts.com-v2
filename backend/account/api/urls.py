from django.urls import path
from account.api.views import (
    PasswordUpdateAPIView,
    UsernameEmailListAPIView,
    # CUSTOMER
    CustomerUserDetailAPIView,
    CustomerRegisterView,
    AddressCreateUpdateDeleteAPIView,
    CustomerUserGeneralInformationUpdate,
    CustomerUserDefaultAddressAPIView,
    # SUPPLIER
    SupplierUserDetailAPIView,
    SupplierRegisterView,
    SupplierUsernameUpdateAPIView,
    SupplierUserProfileImageUpdateAPIView,
    SupplierUserGeneralInformationUpdate,
    SupplierUserAddressUpdateAPIView
)

app_name = 'account'

urlpatterns = [
    path('register/customer/', CustomerRegisterView.as_view(), name='customer_register'),
    path('register/supplier/', SupplierRegisterView.as_view(), name='supplier_register'),

    
    # ! CUSTOMER
    # path('customers/',  CustomerUserListAPIView.as_view(), name='customeruser_list'),
    path('customer/<user__username>/', CustomerUserDetailAPIView.as_view(), name='customer_detail'),
    path('customer/update/information/', CustomerUserGeneralInformationUpdate.as_view(), name='customer_update_information'),
    path('customer/update/default-address/', CustomerUserDefaultAddressAPIView.as_view(), name='customer_update_default_address'),
    path('customer/change/address/', AddressCreateUpdateDeleteAPIView.as_view(), name='customer_change_address'),    

    # ! SUPPLIER
    # path('suppliers/',  SupplierUserListAPIView.as_view(), name='supplier_list'),
    path('supplier/<user__username>/', SupplierUserDetailAPIView.as_view(), name='supplier_detail'),
    path('supplier/update/username/', SupplierUsernameUpdateAPIView.as_view(), name='supplier_update_username'),
    path('supplier/update/image/', SupplierUserProfileImageUpdateAPIView.as_view(), name='supplier_update_image'),
    path('supplier/update/information/', SupplierUserGeneralInformationUpdate.as_view(), name='supplier_update_information'),
    path('supplier/update/address/', SupplierUserAddressUpdateAPIView.as_view(), name='supplier_update_address'),

    #
    path('password/change/', PasswordUpdateAPIView.as_view(), name='password-change'),

    #
    path('informations/verify/', UsernameEmailListAPIView.as_view(), name='verify_list')
    
]