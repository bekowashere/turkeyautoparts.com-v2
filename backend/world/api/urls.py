from django.urls import path
from world.api.views import (
    CountryListAPIView,
    CountryDetailAPIView,
    StateListAPIView,
    CityListAPIView,
    CurrencyListAPIView
)

app_name = 'world'

urlpatterns = [
    # List
    path('countries/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<iso2>', CountryDetailAPIView.as_view(), name='country_detail'),

    #
    path('states/', StateListAPIView.as_view(), name='state_list'),
    path('cities/', CityListAPIView.as_view(), name='city_list'),

    # Currency
    path('currency/', CurrencyListAPIView.as_view(), name='currency_list'),
]
