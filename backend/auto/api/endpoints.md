# auto API endpoints
***
**endpoint:** api/auto/brands/

**method:** GET

**serializer:** BrandListSerializer

**view:** BrandListAPIView

**autoevolution:** /cars


## JSON
```
[
    {
        "id": 1,
        "brand_name": "BMW",
        "brand_slug": "bmw",
        "brand_url": "http://127.0.0.1:8000/api/auto/brands/detail/bmw",
        "brand_detail_url": "https://www.autoevolution.com/bmw/",
        "brand_image": "http://127.0.0.1:8000/images/auto/brands_logo/BMW.jpg",
        "brand_image_url": "https://s1.cdn.autoevolution.com/images/producers/bmw-sm.jpg",
        "brand_in_production_count": 49,
        "brand_discontinued_count": 45,
        "brand_some_series": [
            {
                "id": 1,
                "series_name": "X1",
                "series_slug": "x1"
            },
            {
                "id": 2,
                "series_name": "M8 Coupe",
                "series_slug": "m8-coupe"
            },
            {
                "id": 3,
                "series_name": "8 Series Coupe",
                "series_slug": "8-series-coupe"
            }
        ],
        "translations": {
            "en": {
                "brand_description": ""......""
            },
            "de": {
                "brand_description": ""......""
            },
            "fr": {
                "brand_description": "......"
            }
        }
    }
]

```
***
**endpoint:** api/auto/brands/detail/<brand_slug>

**method:** GET

**serializer:** BrandDetailSerializer

**view:** BrandDetailAPIView

**autoevolution:** /bmw


## JSON
```
{
    "id": 1,
    "brand_name": "BMW",
    "brand_slug": "bmw",
    "brand_image": "http://127.0.0.1:8000/images/auto/brands_logo/BMW.jpg",
    "brand_image_url": "https://s1.cdn.autoevolution.com/images/producers/bmw-sm.jpg",
    "brand_total_series_count": 94,
    "brand_in_production_count": 49,
    "brand_discontinued_count": 45,
    "brand_detail_url": "https://www.autoevolution.com/bmw/",
    "brand_detail_url_en": "https://www.autoevolution.com/bmw/",
    "brand_detail_url_de": "https://www.autoevolution.com/de/autos/bmw/",
    "brand_detail_url_fr": "https://www.autoevolution.com/fr/voitures/bmw/",
    "brand_continued_series": [
        {
            "id": 1,
            "series_name": "X1",
            "series_slug": "x1",
            "series_image": "/images/auto/BMW/X1/X1.jpg",
            "series_image_url": "https://s1.cdn.autoevolution.com/images/models/thumb/BMW_X1-2022_main.jpg_tmb.jpg",
            "series_bodyStyle": "SUVS",
            "series_fuelType": [
                {
                    "id": 1,
                    "type": "Diesel"
                },
                {
                    "id": 2,
                    "type": "Gasoline"
                },
                {
                    "id": 3,
                    "type": "Hybrid"
                },
                {
                    "id": 4,
                    "type": "Mild Hybrid Diesel"
                },
                {
                    "id": 5,
                    "type": "Mild Hybrid"
                }
            ],
            "series_isDiscontinued": false,
            "series_generation_count_bot": 4,
            "series_generation_count": 4,
            "series_generation_oldest_year": 2009,
            "series_generation_newest_year": 2022
        },
    ],
    "brand_discontinued_series": [
        {
            "id": 50,
            "series_name": "1 Series Cabriolet",
            "series_slug": "1-series-cabriolet",
            "series_image": "/images/auto/BMW/1%20Series%20Cabriolet/1%20Series%20Cabriolet.jpg",
            "series_image_url": "https://s1.cdn.autoevolution.com/images/models/thumb/BMW_1-Series-Cabriolet--E88--2010_main.jpg_tmb.jpg",
            "series_bodyStyle": "CONVERTIBLES",
            "series_fuelType": [
                {
                    "id": 1,
                    "type": "Diesel"
                },
                {
                    "id": 2,
                    "type": "Gasoline"
                }
            ],
            "series_isDiscontinued": true,
            "series_generation_count_bot": null,
            "series_generation_count": 2,
            "series_generation_oldest_year": 2008,
            "series_generation_newest_year": 2013
        },
    ]
}
```
***
**endpoint:** api/auto/series/detail/<series_slug>

**method:** GET

**serializer:** SeriesDetailSerializer

**view:** SeriesDetailAPIView

**autoevolution:** /bmw/3-series-sedan/


## JSON
```
...
```
***
**endpoint:** api/auto/models/detail/<model_slug>

**method:** GET

**serializer:** ModelDetailSerializer

**view:** ModelDetailAPIView

**autoevolution:** /cars/bmw-3-series-sedan-2018.html#aeng_bmw-3-series-sedan-g20-2018-320i-8at-184-hp


## JSON
```
...
```
***
**endpoint:** api/auto/cars/detail/<car_slug>

**method:** GET

**serializer:** CarDetailSerializer

**view:** CarDetailAPIView

**autoevolution:** /cars/bmw-3-series-sedan-2018.html#aeng_bmw-3-series-sedan-g20-2018-320i-8at-184-hp


## JSON
```
...
```
***
**endpoint:** api/auto/series/

**method:** GET

**serializer:** SeriesListSerializer

**view:** SeriesListAPIView


## JSON
```
...
```
***
**endpoint:** api/auto/models/

**method:** GET

**serializer:** ModelListSerializer

**view:** ModelListAPIView


## JSON
```
...
```