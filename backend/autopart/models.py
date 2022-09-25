from email.policy import default
from django.db import models
from account.models import SupplierUser
from world.models import Currency
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from auto.models import Car
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import MaxValueValidator, MinValueValidator


# from django_measurement.models import MeasurementField
# from measurement.measures import Weight
# from autopart.units import WeightUnits

def default_image_path():
    return f'autopart/default.png'

# MANUFACTURER [MANN, BOSCH, ORIGINAL..]
def upload_manufacturer_image(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    return f'autopart/manufacturers/{instance.slug}.{extension}'


class Manufacturer(models.Model):
    name = models.CharField(_('Manufacturer Name'), max_length=64)
    slug = models.SlugField(_('Manufacturer Slug'), unique=True)
    code = models.CharField(_('Manufacturer Code'), max_length=5, unique=True)
    image = models.ImageField(
        _('Manufacturer Image'),
        upload_to= upload_manufacturer_image,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    description = models.TextField(_('Manufacturer Description'), null=True, blank=True)

    @property
    def get_all_products(self):
        return self.manufacturer_products.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')


# CAR BRAND [BMW, MERCEDES, AUDI..]
def upload_car_brand_image(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    return f'autopart/car_brands/{instance.slug}.{extension}'

class CarBrand(models.Model):
    name = models.CharField(_('Brand Name'), max_length=64)
    slug = models.SlugField(_('Brand Slug'), unique=True)
    code = models.CharField(_('Brand Code'), max_length=3, unique=True)
    image = models.ImageField(
        _('Brand Image'),
        upload_to= upload_car_brand_image,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    description = models.TextField(_('Brand Description'), null=True, blank=True)

    @property
    def get_all_products(self):
        return self.car_brand_products.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Car Brand')
        verbose_name_plural = _('Car Brands')


# PRODUCT
class ProductSpecification(models.Model):
    name = models.CharField(_('Product Specification'), max_length=128)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Product Specification')
        verbose_name_plural = _('Product Specifications')


# LOOK: path and instance.name or sku,oem,upc +
def upload_product_image(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    return f'autopart/products/{instance.sku}.{extension}'

# LOOK: slug save method - rating, weight..?
class Product(TranslatableModel):
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="manufacturer_products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Manufacturer'),
        help_text="example: MANN-HUMMEL, SWAG, BOSCH.."

    )

    car_brand = models.ForeignKey(
        CarBrand,
        related_name="car_brand_products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Car Brand'),
        help_text="example: AUDI, BMW, MERCEDES.."
    )

    supplier = models.ForeignKey(
        SupplierUser,
        related_name="supplier_products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Supplier'),
        help_text="example: MERCANLAR, DİNAMİK, MARTAŞ.."
    )

    # GENERAL INFORMATION
    oem_code = models.CharField(_('OEM Code'), max_length=128)
    manufacturer_no = models.CharField(_('Manufacturer No'), max_length=128)
    name = models.CharField(_('Product Name'), max_length=255, null=True, blank=True)
    slug = models.SlugField(_('Slug'), unique=True)
    
    # default image = car_brand.image olarak ayarla ?
    """
    image == None > product API image_url;
    - manufacturer.image 
    - manufacturer.name == "ORİJİNAL" > car_brand.image
    """
    image = models.ImageField(
        _('Product Image'),
        upload_to=upload_product_image,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )

    # LOOK: image urlleri url mi? öyleyse URLField
    product_image_url = models.CharField(_('Product Image URL'), max_length=255, null=True, blank=True)

    # MULTIPLE LANGUAGES
    translations = TranslatedFields(
        description = models.TextField(_('Description'), null=True, blank=True)
    )

    # INVENTORY INFORMATION 
    # LOOK: SKU generate and max_length
    sku = models.CharField(_('Stock Keeping Unit'), max_length=32, unique=True)
    upc = models.CharField(_('Universal Product Code'), max_length=12, unique=True, null=True, blank=True)
    moq = models.IntegerField(_('Minimum Order Quantity'), null=True, blank=True)

    # PRICE INFORMATION
    currency = models.ForeignKey(
        Currency,
        related_name="currency_products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Currency'),
    )
    currency_price = models.DecimalField(
        _('Currency Price'),
        max_digits=9,
        decimal_places=2
    )

    # BOT: kdv_net_price_lira
    supplier_net_price = models.DecimalField(
        _('Supplier Net Price (TL)'),
        max_digits=9,
        decimal_places=2
    )
    # supplier_iskonto = models.IntegerField(
    #     _('Supplier İskonto'),
    #     default=0,
    #     validators=[
    #         MinValueValidator(0),
    #         MaxValueValidator(100)
    #     ],
    #     help_text=_('Percentage %')
    # )

    supplier_iskonto = models.CharField(
        _('Supplier İskonto'),
        max_length=32,
        help_text=_('Percentage %')
    )

    # LOOK: Hesaplama supplier_net_price üzerinden yapılıyor (TL)
    price_net = models.DecimalField(
        _('Net Price'),
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True
    )

    # FEATURES
    is_active = models.BooleanField(_('Active'), default=True)
    is_new = models.BooleanField(_('New'), default=False)

    # METADATA
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # CARS - M2M
    # LOOK: brand, series, model, cars filter?
    compatible_cars = models.ManyToManyField(
        Car,
        related_name="products",
        blank=True,
        verbose_name=_('Compatible Cars')
    )
    
    def __str__(self):
        return self.sku

    # LOOK: return image?
    @property
    def image_path(self):
        if self.manufacturer.slug != "orijinal":
            if self.manufacturer.image is not None:
                # Manufacturer image
                return self.manufacturer.image.url
            else:
                if self.car_brand.image is not None:
                    # Brand Image
                    return self.car_brand.image.url
                else:
                    # TAP
                    return f'autopart/default.png'
        else:
            if self.car_brand.image is not None:
                # Brand Image
                return self.car_brand.image.url
            else:
                # TAP
                return f'autopart/default.png'

    @property
    def get_all_specifications(self):
        return self.specifications.all()


    def save(self, *args, **kwargs):
        # CREATE SKU
        supplier_code = self.supplier.code
        brand_code = self.car_brand.code
        manufacturer_code = self.manufacturer.code
        new_sku = f'{supplier_code}-{brand_code}-{manufacturer_code}-{self.oem_code}'
        self.sku = new_sku

        # CREATE NAME
        brand_name = self.car_brand.name
        manufacturer_name = self.manufacturer.name
        new_name = f'{brand_name} {manufacturer_name} {self.oem_code}'
        self.name = new_name

        # CREATE SLUG
        slug = slugify(new_sku)
        self.slug = slug

        super(Product, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductSpecificationValue(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="specifications",
        verbose_name=_('Product')
    )
    specification = models.ForeignKey(
        ProductSpecification,
        on_delete=models.RESTRICT,
        verbose_name=_('Specification')
    )
    value = models.CharField(_('Value'), max_length=255)
    
    
STOCK_STATUS = (
    ('in-stock', _('Available')),
    ('critical', _('Critical')),
    ('en-route', _('Enroute')),
    ('ask', _('Ask')),
    ('out-of-stock', _('Not available')),
)
# Stock
class Stock(models.Model):
    product = models.OneToOneField(
        Product,
        related_name="stock",
        on_delete=models.CASCADE,
        verbose_name=_('Product')
    )

    units = models.IntegerField(_('Units'), default=0)
    units_sold = models.IntegerField(_('Unit Sold'), default=0)

    last_checked_date = models.DateTimeField(
        _('Last Checked Date'),
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=12,
        choices=STOCK_STATUS,
    )

    class Meta:
        verbose_name = _('Product Stock')
        verbose_name_plural = _('Product Stocks')

