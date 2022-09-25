# REST FRAMEWORK
from urllib import request
from rest_framework.response import Response
from rest_framework import status

# REST FRAMEWORK VIEWS
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

# REST FRAMEWORK - JWT
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# PERMISSIONS
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# OUR PERMISSIONS
from account.api.permissions import IsSuperUser, IsSupplier, IsOwnerCustomer

# HELPERS
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from rest_framework.parsers import FileUploadParser
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# OWN HELPERS
from account.validators import validate_phone_number

# MODELS
from account.models import User, CustomerUser, SupplierUser, Address
from world.models import Country

# SERIALIZERS
from account.api.serializers import (
    UserSerializerWithToken,
    SupplierUserSerializer,
    SupplierUserSerializerWithToken,
    AddressSerializer,
    CustomerUserSerializer,
    CustomerUserSerializerWithToken,
    ShippingAddressSerializer,
    UsernameEmailListSerializer,
)

# TOKEN GENERATOR
from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.hashers import check_password

# EMAIL
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# ! USER LOGIN
class MyTokenObtainPairSerializer(TokenObtainSerializer):
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# ! CUSTOMER
# * DETAIL
class CustomerUserDetailAPIView(RetrieveAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field  = 'user__username'

# * CUSTOMER LOGIN
class CustomerUserMyTokenObtainPairSerializer(TokenObtainSerializer):
    def validate(self, attrs):
        data = super(CustomerUserMyTokenObtainPairSerializer, self).validate(attrs)
        customer = CustomerUser.objects.get(user=self.user)

        serializer = CustomerUserSerializerWithToken(customer).data
        for k, v in serializer.items():
            data[k] = v
        return data

class CustomerUserMyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomerUserMyTokenObtainPairSerializer

# * CUSTOMER REGISTER
class CustomerRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        password2 = data.get('password2')

        # edit first_name & last_name for username
        _first_name = first_name.replace("ı", "i")
        _last_name = last_name.replace("ı", "i")

        ex = False
        new_username = slugify(f'c-{_first_name}{_last_name}')
        ex = User.objects.filter(username=new_username).exists()
        while ex:
            new_username = slugify(new_username + " " + get_random_string(9, "0123456789"))
            ex = User.objects.filter(username=new_username).exists()

        username = new_username

        # CONTROL FIELDS
        messages = {'errors': []}

        if email == None:
            messages['errors'].append('Email can not be empty')
        if first_name == None:
            messages['errors'].append('First name can not be empty')
        if last_name == None:
            messages['errors'].append('Last name can not be empty')
        if password == None:
            messages['errors'].append('Password can not be empty')
        if password and password2 and password != password2:
            messages['errors'].append('Passwords do not be match')
        if User.objects.filter(email=email).exists():
            messages['errors'].append('Account already exists with this email')
        if User.objects.filter(username=username).exists():
            messages['errors'].append('Account already exists with this username')
        if len(messages['errors']) > 0:
            return Response({'status':'error', 'detail': messages['errors']}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                first_name=first_name,
                last_name=last_name,
                is_customer=True
            )

            customer = CustomerUser.objects.create(user=user)
            serializer = CustomerUserSerializerWithToken(customer, many=False)
        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'success', 'user':serializer.data}, status=status.HTTP_200_OK)

# * CHANGE -> CUSTOMER GENERAL INFORMATION
class CustomerUserGeneralInformationUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        data = request.data
        user = request.user

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone_number')

        try:
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            customer = CustomerUser.objects.get(user=user)
            customer.phone_number = phone_number
            customer.save()
            
            serializer = CustomerUserSerializer(customer, many=False)
        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'success', 'user': serializer.data}, status=status.HTTP_200_OK)

# * ADDRESS
class CustomerUserDefaultAddressAPIView(APIView):
    permission_classes = [IsOwnerCustomer]

    def put(self, request):
        data = request.data
        user = request.user

        address_id = data.get('address_id')

        try:
            customer = CustomerUser.objects.get(user=user)
            address = Address.objects.get(id=address_id)
            customer.default_shipping_address = address
            customer.save()
            
            serializer = ShippingAddressSerializer(address)
        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'success', 'detail': 'Default Shipping Address changed successfully', 'address':serializer.data}, status=status.HTTP_200_OK)

class AddressCreateUpdateDeleteAPIView(APIView):
    permission_classes = [IsOwnerCustomer]

    def post(self, request):

        data = request.data
        user = request.user

        address_name = data.get('address_name')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        company_name = data.get('company_name')
        phone_number = data.get('phone_number')
        street_address_1 = data.get('street_address_1')
        street_address_2 = data.get('street_address_2')
        postal_code = data.get('postal_code')
        city = data.get('city')
        city_area = data.get('city_area')
        _country = data.get('country')

        # GET COUNTRY OBJECT
        country = Country.objects.get(id=_country)

        try:
            customerUser = CustomerUser.objects.get(user=user)

            address = Address.objects.create(
                user=customerUser,
                address_name=address_name,
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                phone_number=phone_number,
                street_address_1=street_address_1,
                street_address_2=street_address_2,
                postal_code=postal_code,
                city=city,
                city_area=city_area,
                country=country
            )

            if customerUser.default_shipping_address is None:
                customerUser.default_shipping_address = address
            
            customerUser.save()

            serializer = ShippingAddressSerializer(address)

        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'success', 'address':serializer.data}, status=status.HTTP_200_OK)


    def put(self, request):
        data = request.data
        user = request.user

        address_id = data.get('address_id')
        address_name = data.get('address_name')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        company_name = data.get('company_name')
        phone_number = data.get('phone_number')
        street_address_1 = data.get('street_address_1')
        street_address_2 = data.get('street_address_2')
        postal_code = data.get('postal_code')
        city = data.get('city')
        city_area = data.get('city_area')
        _country = data.get('country')

        # GET COUNTRY OBJECT
        country = Country.objects.get(id=_country)

        try:
            address = Address.objects.get(id=address_id)
            address.address_name = address_name
            address.first_name = first_name
            address.last_name = last_name
            address.company_name = company_name
            address.phone_number = phone_number
            address.street_address_1 = street_address_1
            address.street_address_2 = street_address_2
            address.postal_code = postal_code
            address.city = city
            address.city_area = city_area
            address.country = country

            address.save()

            serializer = ShippingAddressSerializer(address)

        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'success', 'detail': 'Address changed successfully', 'address':serializer.data}, status=status.HTTP_200_OK)

    
    def delete(self, request):
        data = request.data
        address_id = data.get('address_id')

        try:
            address = Address.objects.get(id=address_id)
            address.delete()

        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'success', 'detail': 'Address deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        

# ! SUPPLIER
# * DETAIL
class SupplierUserDetailAPIView(RetrieveAPIView):
    queryset = SupplierUser.objects.all()
    serializer_class = SupplierUserSerializer
    # permission_classes = []
    lookup_field = 'user__username'

# * SUPPLIER LOGIN
class SupplierUserMyTokenObtainPairSerializer(TokenObtainSerializer):
    def validate(self, attrs):
        data = super(SupplierUserMyTokenObtainPairSerializer, self).validate(attrs)
        supplier = SupplierUser.objects.get(user=self.user)

        serializer = SupplierUserSerializerWithToken(supplier).data
        for k, v in serializer.items():
            data[k] = v
        return data

class SupplierUserMyTokenObtainPairView(TokenObtainPairView):
    serializer_class = SupplierUserMyTokenObtainPairSerializer

# * SUPPLIER REGISTER
class SupplierRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')
        company_name = data.get('company_name')
        code = data.get('code')

        ex = False
        new_username = slugify(company_name)
        ex = User.objects.filter(username=new_username).exists()
        while ex:
            new_username = slugify(f"{new_username} {get_random_string(9, '0123456789')}")
            ex = User.objects.filter(username=new_username).exists()

        username = new_username
        supplier_slug = new_username

        messages = {'errors': []}

        if email == None:
            messages['errors'].append('Email can not be empty')
        if password == None:
            messages['errors'].append('Password can not be empty')
        if password and password2 and password != password2:
            messages['errors'].append('Passwords can not be match')
        
        if company_name == None:
            messages['errors'].append('Company Name can not be empty')
        if SupplierUser.objects.filter(company_name=company_name).exists():
            messages['errors'].append('Supplier already exists with this company name')
        
        if code == None:
            messages['errors'].append('Company code can not be empty')
        if SupplierUser.objects.filter(code=code).exists():
            messages['errors'].append('Supplier already exists with this company code')
        
        if User.objects.filter(email=email).exists():
            messages['errors'].append('Account already exists with this email')
        if User.objects.filter(username=username).exists():
            messages['errors'].append('Account already exists with this username')
        if len(messages['errors']) > 0:
            return Response({'status':'error', 'detail': messages['errors']}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                is_supplier=True
            )

            # is_verified -> default = False
            supplier = SupplierUser.objects.create(
                user=user,
                company_name=company_name,
                code=code,
                supplier_slug=supplier_slug
            )

            serializer = SupplierUserSerializerWithToken(supplier, many=False)

        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'success', 'user':serializer.data}, status=status.HTTP_200_OK)

class SupplierUsernameUpdateAPIView(APIView):
    permission_classes = [IsSupplier]

    def put(self, request):
        data = request.data
        user = request.user
        current_username = user.username

        new_username = data.get('username')

        messages = {'errors': []}

        if new_username == None:
            messages['errors'].append('Username can not be empty')
        if new_username == current_username:
            messages['errors'].append('Username must be different')
        if User.objects.filter(username=new_username).exists():
            messages['errors'].append('Account already exists with this username')
        if len(messages['errors']) > 0:
            return Response({'status':'error', 'detail': messages['errors']}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user.username = new_username
            user.save()

            serializer = UsernameEmailListSerializer(user, many=False)

        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'success', 'user': serializer.data}, status=status.HTTP_200_OK)

# * CHANGE IMAGE
class SupplierUserProfileImageUpdateAPIView(APIView):
    permission_classes = [IsSupplier]

    # parser_classes = [FileUploadParser]

    def put(self, request):
        data = request.data
        user = request.user

        new_image = request.FILES.get('profile_image')

        try:
            supplier = SupplierUser.objects.get(user=user)
            supplier.company_image = new_image
            supplier.save()
        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'success', 'detail': 'Profile image changed successfully'}, status=status.HTTP_200_OK)




# * CHANGE -> SUPPLIER GENERAL INFORMATION - PROFILE
class SupplierUserGeneralInformationUpdate(APIView):
    permission_classes = [IsSupplier]

    def put(self, request):
        data = request.data
        user = request.user

        company_name = data.get('company_name')
        code = data.get('code')
        description = data.get('description')
        website_url = data.get('website_url')
        public_phone_number = data.get('public_phone_number')
        public_email = data.get('public_email')
        fax_number = data.get('fax_number')

        try:
            supplier = SupplierUser.objects.get(user=user)
            supplier.company_name = company_name
            supplier.code = code
            supplier.description = description
            supplier.website_url = website_url
            supplier.public_phone_number = public_phone_number
            supplier.public_email = public_email
            supplier.fax_number = fax_number
            supplier.save()
            serializer = SupplierUserSerializer(supplier, many=False)
        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'success', 'user': serializer.data}, status=status.HTTP_200_OK)

# * CHANGE -> SUPPLIER ADDRESS INFORMATION
class SupplierUserAddressUpdateAPIView(APIView):
    permission_classes = [IsSupplier]
    def put(self, request):
        data = request.data
        user= request.user

        street_address_1 = data.get('street_address_1')
        street_address_2 = data.get('street_address_2')
        postal_code = data.get('postal_code')
        city = data.get('city')
        city_area = data.get('city_area')
        _country = data.get('country')

        try:
            supplier = SupplierUser.objects.get(user=user)
            country = Country.objects.get(id=_country)
            supplier.street_address_1 = street_address_1
            supplier.street_address_2 = street_address_2
            supplier.postal_code = postal_code
            supplier.city = city
            supplier.city_area = city_area
            supplier.country = country
            supplier.save()
            serializer = SupplierUserSerializer(supplier, many=False)
        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'success', 'user': serializer.data}, status=status.HTTP_200_OK)



# ! ORTAK
# * CHANGE USERNAME
class UsernameEmailListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsernameEmailListSerializer

# * CHANGE PASSWORD
class PasswordUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        data = request.data
        user = request.user

        old_password = data.get('old_password')
        new_password = data.get('new_password')
        new_password_confirm = data.get('new_password_confirm')

        valid = user.check_password(old_password)

        messages = {'errors': []}

        if not valid:
            messages['errors'].append('Old password is not true')
        if new_password is None:
            messages['errors'].append('New password field required')
        if new_password_confirm is None:
            messages['errors'].append('New password confirm field required')
        if new_password and new_password_confirm:
            if new_password == new_password_confirm:
                user.set_password(new_password)
                user.save()
                return Response({'status': 'success', 'detail': 'Password changed successfully'}, status=status.HTTP_200_OK)
            else:
                messages['errors'].append('Passwords do not match')
        if len(messages['errors']) > 0:
            return Response({'status':'error', 'detail': messages['errors']}, status=status.HTTP_400_BAD_REQUEST)

