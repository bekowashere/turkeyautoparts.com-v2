from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin

from autopart.models import (
    Manufacturer,
    CarBrand, 
    Product,
    ProductSpecificationValue,
    Stock
)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Basic Information'), {'fields': ('name','slug')}),
        (_('Image'), {'fields': ('image',)}),
        (_('Description'), {'fields': ('description',)})
    )

    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    
@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Basic Information'), {'fields': ('name','slug')}),
        (_('Image'), {'fields': ('image',)}),
        (_('Description'), {'fields': ('description',)})
    )

    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')

class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    fieldsets = (
        (_('General Information'), {'fields': ('oem_code', 'name', 'slug')}),
        (_('Image'), {'fields': ('image',)}),
        (_('Relations'), {'fields': ('manufacturer', 'car_brand', 'supplier')}),
        (_('Inventory Information'), {'fields': ('sku', 'upc', 'moq')}),
        (_('Price Information'), {'fields': ('supplier_net_price', 'supplier_iskonto', 'currency_price', 'price_net')}),
        (_('Description'), {'fields': ('description',)}),
        (_('Features'), {'fields': ('is_active', 'is_new')}),
        (_('Compatibility'), {'fields': ('compatible_cars',)}),
        (_('Metadata'), {'fields': ('updated_date', 'created_date')}),
    )

    list_display = ('oem_code', 'sku', 'upc', 'name', 'slug')
    list_filter = ('manufacturer__name', 'car_brand__name', 'is_active', 'is_new')
    search_fields = ('oem_code', 'sku', 'upc', 'name', 'slug')
    readonly_fields = ('updated_date', 'created_date')

    inlines = [
        ProductSpecificationValueInline
    ]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Product'), {'fields': ('product',)}),
        (_('Stock Information'), {'fields': ('units', 'units_sold', 'last_checked_date')}),
        (_('Status'), {'fields': ('status',)}),
    )

    list_display = ('units', 'units_sold', 'last_checked_date')
    list_filter = ('status',)
    search_fields = ('product__oem_code', 'products__sku', 'product__upc', 'product__name', 'product__slug')
    