from django.db import models
import uuid
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# PHONE
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField
from account.validators import validate_possible_number

# WORLD
from world.models import Language, Country

class PossiblePhoneNumberField(PhoneNumberField):
    default_validators = [validate_possible_number]


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with given email and password
        """

        if not email:
            raise ValueError(_('You must provide an email address'))

        if not password:
            raise ValueError(_('User must have a password'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self._create_user(email, password=password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        user = self._create_user(email, password=password, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('Username'),
        max_length=128,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('Email Address'),
        unique=True,
        help_text=_('Required. 50 characters or fewer. Example: john.doe@gmail.com'),
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )

    first_name = models.CharField(_('First Name'), max_length=64, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=64, blank=True)

    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff User'), default=False)
    is_superuser = models.BooleanField(_('Superuser'), default=False)

    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    last_login = models.DateTimeField(auto_now=True)

    #
    is_customer = models.BooleanField(_('Customer'), default=False)
    is_supplier = models.BooleanField(_('Supplier'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_username()

    def get_full_name(self):
        """
        Return the first_name + last_name
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        'account.CustomerUser',
        on_delete=models.CASCADE,
        related_name='customer_addresses',
        verbose_name=_('Customer')
    )
    address_name = models.CharField(_('Address Name'), max_length=64, help_text="Ex: Home")
    first_name = models.CharField(_('First Name'), max_length=64)
    last_name = models.CharField(_('Last Name'), max_length=64)
    company_name = models.CharField(_('Company Name'), max_length=64, null=True, blank=True)

    phone_number = PossiblePhoneNumberField(null=True, blank=True, verbose_name=_('Phone'))

    # Address Information
    street_address_1 = models.CharField(_('Street Address 1'), max_length=256)
    street_address_2 = models.CharField(_('Street Address 2'), max_length=256, null=True, blank=True)
    postal_code = models.CharField(_('Postal Code'), max_length=32)
    city = models.CharField(_('City'), max_length=64, help_text="Ex: Los Angeles")
    city_area = models.CharField(_('City Area'), max_length=64, help_text="Ex: California")

    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        related_name='adddress_country',
        verbose_name=_('Country'),
        null=True
    )

    def __str__(self):
        if self.company_name:
            return f'{self.address_name} - {self.company_name}'
        return self.address_name

    @property
    def full_name(self):
        """
        Return the first_name + last_name
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class CustomerUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_('User')
    )
    phone_number = PossiblePhoneNumberField(null=True, blank=True, verbose_name='Phone')

    default_shipping_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        related_name='shipping_address',
        null=True,
        blank=True,
        verbose_name=_('Default Shipping Address')
    )
    note = models.TextField(_('Note'), null=True, blank=True)

    def __str__(self):
        return self.user.email

    @property
    def get_all_addresses(self):
        return self.customer_addresses.all()

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

# Supplier User : Mercanlar, Dinamik, Martaş
def default_supplier_image_path():
    return f'account/suppliers/default.png'

def upload_supplier_image(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    return f'account/suppliers/{instance.user}/main_image.{extension}'

class SupplierUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_('User')
    )
    company_image = models.ImageField(
        _('Company Image'),
        upload_to=upload_supplier_image,
        default=default_supplier_image_path,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    company_name = models.CharField(_('Company Name'), max_length=128)
    supplier_slug = models.SlugField(_('Slug'))
    code = models.CharField(_('Company Code'), max_length=4, unique=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    website_url = models.URLField(_('Website'), null=True, blank=True, help_text='www.my-site.com')

    # Contact Fields
    # phone_number for account management (reset password, send sms..)
    # public_phone_number for everyone
    phone_number = PossiblePhoneNumberField(null=True, blank=True, verbose_name=_('Hidden Phone'))
    public_phone_number = PossiblePhoneNumberField(null=True, blank=True, verbose_name=_('Public Phone'))
    public_email = models.EmailField(_('Email Address'), null=True, blank=True)
    fax_number = PossiblePhoneNumberField(null=True, blank=True, verbose_name=_('Fax'))

    # Location
    street_address_1 = models.CharField(_('Street Address 1'), max_length=256, null=True, blank=True)
    street_address_2 = models.CharField(_('Street Address 2'), max_length=256, null=True, blank=True)
    postal_code = models.CharField(_('Postal Code'), max_length=32, null=True, blank=True)
    city = models.CharField(_('City'), max_length=64, null=True, blank=True, help_text="Ex: Los Angeles")
    city_area = models.CharField(_('City Area'), max_length=64, null=True, blank=True, help_text="Ex: California")
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        related_name='s_addresses',
        verbose_name=_('Country'),
        null=True,
        blank=True
    )
    latitude = models.DecimalField(_('Latitude'), max_digits=11, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(_('Longitude'), max_digits=11, decimal_places=8, null=True, blank=True)

    is_verified = models.BooleanField(_('Verified'), default=False)

    languages = models.ManyToManyField(
        Language,
        verbose_name=_('Languages'),
        help_text=_('Select spoken languages'),
        blank=True
    )

    # TO-DO
    # rating
    # get_products
    # get_products_count
    # get_comments

    def __str__(self):
        return self.company_name

    class Meta:
        # ordering rating
        ordering = ('company_name',)
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')