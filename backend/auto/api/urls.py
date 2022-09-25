from django.urls import path
from auto.api.views import (
    BrandListAPIView,
    BrandDetailAPIView,
    SeriesListAPIView,
    SeriesDetailAPIView,
    ModelListAPIView,
    ModelDetailAPIView,
    CarDetailAPIView,
)

app_name = 'auto'

urlpatterns = [
    # List
    # CARS
    path('brands/', BrandListAPIView.as_view(), name='brand_list'),
    path('series/', SeriesListAPIView.as_view(), name='series_list'),
    path('models/', ModelListAPIView.as_view(), name='model_list'),

    # Detail
    # BMW
    path('brands/detail/<brand_slug>', BrandDetailAPIView.as_view(), name='brand_detail'),
    # BMW/1 SERIES
    path('series/detail/<series_slug>', SeriesDetailAPIView.as_view(), name='series_detail'),
    # BMW/1 SERIES/F40
    path('models/detail/<model_slug>', ModelDetailAPIView.as_view(), name='model_detail'),
    path('cars/detail/<car_slug>', CarDetailAPIView.as_view(), name='car_detail'),
]