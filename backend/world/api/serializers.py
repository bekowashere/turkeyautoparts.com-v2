from rest_framework import serializers
from world.models import Country, Currency, Timezone


# ! Country 
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'currency_code', 'currency_name', 'currency_symbol')


class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ('id', 'zoneName', 'gmtOffset', 'gmtOffsetName', 'abbreviation', 'tzName')

class CountryDetailSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    timezones = TimezoneSerializer(many=True)

    class Meta:
        model = Country
        fields = (
            'id',
            'name',
            'iso3',
            'iso2',
            'numeric_code',
            'phone_code',
            'capital',
            'currency',
            'timezones',
            'region',
            'subregion',
            'latitude',
            'longitude'
        )

# ! Country id-name-iso2
class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'iso2')