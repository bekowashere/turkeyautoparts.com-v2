from django.urls import path
from autopart.api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    ManufacturerListAPIView,
    ManufacturerDetailAPIView,
    CarBrandListAPIView,
    CarBrandDetailAPIView,
)

app_name = 'autopart'

urlpatterns = [
    # List
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('manufacturers/', ManufacturerListAPIView.as_view(), name='manufacturer_list'),
    path('brands/', CarBrandListAPIView.as_view(), name='brand_list'),

    # Detail
    path('product/<slug>', ProductDetailAPIView.as_view(), name='product_detail'),
    path('manufacturer/<slug>', ManufacturerDetailAPIView.as_view(), name='manufacturer_detail'),
    path('brand/<slug>', CarBrandDetailAPIView.as_view(), name='brand_detail'),



]