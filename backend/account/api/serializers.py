from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# MODELS
from account.models import User, CustomerUser, SupplierUser, Address


# ADDRESS
class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    def get_country(self, obj):
        return obj.country.name

    class Meta:
        model = Address
        fields = ('id', 'address_name', 'country')

# USER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'is_active', 'is_customer', 'is_supplier'
        )


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        # return str(token)
        return str(token.access_token)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'is_active', 'is_customer', 'is_supplier', 'token'
        )

# CUSTOMER USER
class CustomerUserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    is_customer = serializers.SerializerMethodField()
    default_shipping_address = AddressSerializer()
    addresses = serializers.SerializerMethodField()

    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_is_active(self, obj):
        return obj.user.is_active

    def get_is_customer(self, obj):
        return obj.user.is_customer

    def get_addresses(self, obj):
        return ShippingAddressSerializer(obj.get_all_addresses, many=True).data

    class Meta:
        model = CustomerUser
        fields = (
            'user',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_customer',
            'phone_number',
            'note',
            'default_shipping_address',
            'addresses'
        )

class CustomerUserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    is_customer = serializers.SerializerMethodField()
    default_shipping_address = AddressSerializer()
    addresses = serializers.SerializerMethodField()

    def get_token(self, obj):
        token = RefreshToken.for_user(obj.user)
        return str(token.access_token)

    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_is_active(self, obj):
        return obj.user.is_active

    def get_is_customer(self, obj):
        return obj.user.is_customer

    def get_addresses(self, obj):
        return ShippingAddressSerializer(obj.get_all_addresses, many=True).data

    class Meta:
        model = CustomerUser
        fields = (
            'user',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_customer',
            'token',
            'phone_number',
            'note',
            'default_shipping_address',
            'addresses'
        )

# SUPPLIER USER
class SupplierUserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    is_supplier = serializers.SerializerMethodField()

    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username

    def get_is_active(self, obj):
        return obj.user.is_active

    def get_is_supplier(self, obj):
        return obj.user.is_supplier

    class Meta:
        model = SupplierUser
        fields = (
            'user',
            'email',
            'username',
            'is_active',
            'is_supplier',
            'is_verified',
            'company_name',
            'supplier_slug',
            'code',
            'description',
            'website_url',
            'phone_number',
            'public_phone_number',
            'public_email',
            'fax_number',
            'street_address_1',
            'street_address_2',
            'postal_code',
            'city',
            'city_area',
            'country',
            'latitude',
            'longitude',
            'is_verified',
            'languages', 
        )

class SupplierUserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    is_supplier = serializers.SerializerMethodField()

    def get_token(self, obj):
        token = RefreshToken.for_user(obj.user)
        return str(token.access_token)

    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username

    def get_is_active(self, obj):
        return obj.user.is_active

    def get_is_supplier(self, obj):
        return obj.user.is_supplier

    class Meta:
        model = SupplierUser
        fields = (
            'user',
            'email',
            'username',
            'is_active',
            'is_supplier',
            'is_verified',
            'token',
            'company_name',
            'supplier_slug',
            'code',
            'description',
            'website_url',
            'phone_number',
            'public_phone_number',
            'public_email',
            'fax_number',
            'street_address_1',
            'street_address_2',
            'postal_code',
            'city',
            'city_area',
            'country',
            'latitude',
            'longitude',
            'is_verified',
            'languages', 
        )

# USERNAME SERIALIZER
class UsernameEmailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')