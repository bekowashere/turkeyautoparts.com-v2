from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import User, CustomerUser, SupplierUser, Address
from account.forms import CustomUserCreationForm

@admin.register(User)
class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    fieldsets = (
        (_('Login Information'), {'fields': ('email', 'username', 'password')}),
        (_('Personal Information'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_supplier', 'groups', 'user_permissions'
            )
        }),
        (_('Dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # ADD USER FIELD
    add_fieldsets = (
        (_('Login Information'), {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)
    filter_horizontal = (
        'groups',
        'user_permissions',
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Address Personal Information'),
         {'fields': ('address_name', 'first_name', 'last_name', 'company_name', 'phone_number')}),
        (_('Address'), {
            'fields': ('street_address_1', 'street_address_2', 'postal_code', 'city', 'city_area', 'country')
        })
    )

    list_display = ('address_name', 'user', 'city', 'city_area', 'country')
    search_fields = ('address_name', 'user__email__icontains', 'city', 'city_area', 'country__name__icontains')


@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Personal Information'), {'fields': ('phone_number',)}),
        (_('Default Addresses'), {'fields': ('default_shipping_address',)}),
        (_('Note'), {'fields': ('note',)}),
    )

    list_display = ('user', 'phone_number')
    search_fields = ('user__email__icontains',)

@admin.register(SupplierUser)
class SupplierUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Supplier Information'), {'fields': ('company_name', 'supplier_slug', 'code', 'phone_number', 'company_image', 'website_url')}),
        (_('Contact Information'), {'fields': ('public_phone_number', 'fax_number')}),
        (_('Location Information'), {'fields': ('street_address_1', 'street_address_2', 'postal_code', 'city', 'city_area', 'country', 'latitude', 'longitude')}),
        (_('Verify'), {'fields': ('is_verified',)}),
        (_('Languages'), {'fields': ('languages',)}),
    )

    list_display = ('user', 'company_name', 'website_url')
    list_filter = ('is_verified',)
    search_fields = ('user__email__icontains', 'company_name','website_url', 'supplier_slug')