from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from world.models import Country, Currency
from world.api.serializers import CountryListSerializer, CountryDetailSerializer, CurrencySerializer
import json

class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

class CountryDetailAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    lookup_field = 'iso2'


class StateListAPIView(APIView):
    """
    {
        "id": 2170,
        "name": "Istanbul",
        "country_id": 225,
        "country_code": "TR",
        "country_name": "Turkey",
        "state_code": "34",
        "type": "province",
        "latitude": "41.16343020",
        "longitude": "28.76644080"
    }
    """

    def get(self, request):
        file_path = '_data/world/states.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        country_code = self.request.query_params.get('country_code')
        # http://127.0.0.1:8000/api/world/cities/?country_code=TR

        queryset = []
        if country_code is not None:
            for state in data:
                if state['country_code'] == country_code:
                    queryset.append(state)
            return Response(queryset)

        return Response(data)

class CityListAPIView(APIView):
    """
    {
        "id": 107622,
        "name": "Eyüpsultan",
        "state_id": 2170,
        "state_code": "34",
        "state_name": "Istanbul",
        "country_id": 225,
        "country_code": "TR",
        "country_name": "Turkey",
        "latitude": "41.19904000",
        "longitude": "28.88667000",
        "wikiDataId": "Q673073"
    }
    """

    def get(self, request):
        file_path = '_data/world/cities.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        country_code = self.request.query_params.get('country_code')
        state_code = self.request.query_params.get('state_code')
        # http://127.0.0.1:8000/api/world/cities/?country_code=TR&state_code=34

        queryset = []
        if country_code is not None and state_code is not None:
            for city in data:
                if city['country_code'] == country_code and city['state_code'] == state_code:
                    queryset.append(city)
            return Response(queryset)

        return Response(data)


# CURRENCY
class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer