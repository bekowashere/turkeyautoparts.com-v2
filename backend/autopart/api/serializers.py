from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from account.models import SupplierUser
from autopart.models import (
    Manufacturer,
    CarBrand,
    Product,
    ProductSpecificationValue,
    Stock
)
from auto.models import Car
from world.models import Currency


# ! PRODUCT
# PRODUCT HELPER SERIALIZER
class AutoSeriliazer(serializers.ModelSerializer):
    car_brand = serializers.SerializerMethodField()
    car_series = serializers.SerializerMethodField()
    car_model = serializers.SerializerMethodField()

    def get_car_brand(self, obj):
        return obj.car_brand.brand_name

    def get_car_series(self, obj):
        return obj.car_series.series_name

    def get_car_model(self, obj):
        return obj.car_model.model_name

    class Meta:
        model = Car
        fields = ('car_brand', 'car_series', 'car_model', 'id', 'car_name', 'car_slug')

class ProductManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'slug', 'code')

class ProductCarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('id', 'name', 'slug', 'code')

class ProductSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierUser
        fields = ('user', 'company_name', 'supplier_slug', 'code')

class ProductCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'currency_code', 'currency_name', 'currency_symbol')


class ProductListSerializer(serializers.ModelSerializer):
    manufacturer = ProductManufacturerSerializer()
    car_brand = ProductCarBrandSerializer()
    supplier = ProductSupplierSerializer()
    currency = ProductCurrencySerializer()

    class Meta:
        model = Product
        # depth = 2
        fields = (
            'id',
            'name',
            'oem_code',
            'sku',
            'upc',
            'slug',
            'manufacturer',
            'manufacturer_no',
            'car_brand',
            'supplier',
            'image',
            'product_image_url',
            'image_path',
            'moq',
            
            'currency',
            'currency_price',
            'supplier_net_price',
            'price_net',
            'supplier_iskonto',
        )

class ProductSpecificationValueSerializer(serializers.ModelSerializer):
    specification = serializers.SerializerMethodField()

    def get_specification(self, obj):
        return obj.specification.name

    class Meta:
        model = ProductSpecificationValue
        fields = ('specification', 'value')

class ProductDetailSerializer(TranslatableModelSerializer):
    manufacturer = ProductManufacturerSerializer()
    car_brand = ProductCarBrandSerializer()
    supplier = ProductSupplierSerializer()
    currency = ProductCurrencySerializer()
    compatible_cars = AutoSeriliazer(read_only=True, many=True)
    specifications = serializers.SerializerMethodField()
    translations = TranslatedFieldsField(shared_model=Product)

    def get_specifications(self, obj):
        return ProductSpecificationValueSerializer(obj.get_all_specifications, many=True).data

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'oem_code',
            'sku',
            'upc',
            'manufacturer',
            'manufacturer_no',
            'car_brand',
            'supplier',
            'image',
            'product_image_url',
            'image_path',
            'moq',
            'currency',
            'currency_price',
            'supplier_net_price',
            'price_net',
            'supplier_iskonto',
            'translations',
            'specifications',
            'compatible_cars',
        )

# ! MANUFACTURER
class ManufacturerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'slug', 'code', 'image')

class ManufacturerDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return ProductListSerializer(obj.get_all_products, many=True).data

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'slug', 'code', 'image', 'description', 'products')

# ! CAR BRAND
class CarBrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('id', 'name', 'slug', 'code', 'image')

class CarBrandDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return ProductListSerializer(obj.get_all_products, many=True).data

    class Meta:
        model = CarBrand
        fields = ('id', 'name', 'slug', 'code', 'image', 'description', 'products')

