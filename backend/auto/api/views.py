# Rest Framework Views
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

# Rest Framework Filters
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework Helpers
from rest_framework.response import Response
from rest_framework import status

from auto.models import Brand, Series, Model, Car

from auto.api.serializers import (
    BrandListSerializer,
    BrandDetailSerializer,
    SeriesListSerializer,
    SeriesDetailSerializer,
    ModelListSerializer,
    ModelDetailSerializer,
    CarDetailSerializer
)

# ! BRAND
class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer


class BrandDetailAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer
    lookup_field = 'brand_slug'

# ! SERIES
class SeriesListAPIView(ListAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesListSerializer

class SeriesDetailAPIView(RetrieveAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesDetailSerializer
    lookup_field = 'series_slug'

# ! MODEL
class ModelListAPIView(ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelListSerializer

class ModelDetailAPIView(RetrieveAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelDetailSerializer
    lookup_field = 'model_slug'

# ! CAR
class CarDetailAPIView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    lookup_field = 'car_slug'