# Rest Framework Views
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from autopart.api.paginations import ProductPagination, ManufacturerPagination, CarBrandPagination

# Rest Framework Filters
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from autopart.models import (
    Manufacturer,
    CarBrand,
    Product
)

from autopart.api.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    ManufacturerListSerializer,
    ManufacturerDetailSerializer,
    CarBrandListSerializer,
    CarBrandDetailSerializer
)

# ! PRODUCT
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['compatible_cars__id', 'compatible_cars__car_brand']
    pagination_class = ProductPagination

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'

# ! MANUFACTURER
class ManufacturerListAPIView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerListSerializer
    pagination_class = ManufacturerPagination

class ManufacturerDetailAPIView(RetrieveAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerDetailSerializer
    lookup_field = 'slug'

# ! CARBRAND
class CarBrandListAPIView(ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandListSerializer
    pagination_class = CarBrandPagination

class CarBrandDetailAPIView(RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandDetailSerializer
    lookup_field = 'slug'


