# autopart API endpoints
***
**endpoint:** api/autopart/products/

**method:** GET

**serializer:** ProductListSerializer

**view:** ProductListAPIView


## JSON
```
{
    "count": 87,
    "next": "http://127.0.0.1:8000/api/autopart/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "AUDI ERA 06A919501A",
            "oem_code": "06A919501A",
            "sku": "MERC-AUD3-ERA43-06A919501A",
            "upc": null,
            "slug": "audi-era-06a919501a-merc-aud3-era43-06a919501a",
            "manufacturer": {
                "id": 43,
                "name": "ERA",
                "slug": "era",
                "code": "ERA43"
            },
            "manufacturer_no": "E-330546",
            "car_brand": {
                "id": 3,
                "name": "AUDI",
                "slug": "audi",
                "code": "AUD3"
            },
            "supplier": {
                "user": 2,
                "company_name": "Mercanlar",
                "supplier_slug": "mercanlar",
                "code": "MERC"
            },
            "image": null,
            "product_image_url": null,
            "image_path": "/images/autopart/default.png",
            "moq": null,
            "currency": {
                "id": 2,
                "currency_code": "EUR",
                "currency_name": "Euro",
                "currency_symbol": "€"
            },
            "currency_price": 4.34,
            "supplier_net_price": 71.04,
            "price_net": 78.14,
            "supplier_iskonto": "%20+5"
        }
    ]
}
```
***
**endpoint:** api/autopart/product/<slug>/

**method:** GET

**serializer:** ProductDetailSerializer

**view:** ProductDetailAPIView


## JSON
```
{
    "id": 1,
    "name": "AUDI ERA 06A919501A",
    "slug": "audi-era-06a919501a-merc-aud3-era43-06a919501a",
    "oem_code": "06A919501A",
    "sku": "MERC-AUD3-ERA43-06A919501A",
    "upc": null,
    "manufacturer": {
        "id": 43,
        "name": "ERA",
        "slug": "era",
        "code": "ERA43"
    },
    "manufacturer_no": "E-330546",
    "car_brand": {
        "id": 3,
        "name": "AUDI",
        "slug": "audi",
        "code": "AUD3"
    },
    "supplier": {
        "user": 2,
        "company_name": "Mercanlar",
        "supplier_slug": "mercanlar",
        "code": "MERC"
    },
    "image": null,
    "product_image_url": null,
    "image_path": "/images/autopart/default.png",
    "moq": null,
    "currency": {
        "id": 2,
        "currency_code": "EUR",
        "currency_name": "Euro",
        "currency_symbol": "€"
    },
    "currency_price": 4.34,
    "supplier_net_price": 71.04,
    "price_net": 78.14,
    "supplier_iskonto": "%20+5",
    "translations": {},
    "specifications": [],
    "compatible_cars": []
}
```
***
**endpoint:** api/autopart/manufacturers/

**method:** GET

**serializer:** ManufacturerListSerializer

**view:** ManufacturerListAPIView


## JSON
```
{
    "count": 176,
    "next": "http://127.0.0.1:8000/api/autopart/manufacturers/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "ABA",
            "slug": "aba",
            "code": "ABA1",
            "image": "http://127.0.0.1:8000/images/autopart/default.png"
        },
        {
            "id": 2,
            "name": "AIR FLOW",
            "slug": "air-flow",
            "code": "AIR2",
            "image": "http://127.0.0.1:8000/images/autopart/default.png"
        }
    ]
}

```
***
**endpoint:** api/autopart/manufacturer/<slug>/

**method:** GET

**serializer:** ManufacturerDetailSerializer

**view:** ManufacturerDetailAPIView


## JSON
```
{
    "id": 98,
    "name": "MANN-HUMMEL",
    "slug": "mann-hummel",
    "code": "MAN98",
    "image": "http://127.0.0.1:8000/images/autopart/Manufacturer/MANN-HUMMEL.png",
    "description": null,
    "products": [
        {
            "id": 59,
            "name": "BMW MANN-HUMMEL 11427640862",
            "oem_code": "11427640862",
            "sku": "MERC-BMW5-MAN98-11427640862",
            "upc": null,
            "slug": "bmw-mann-hummel-11427640862-merc-bmw5-man98-11427640862",
            "manufacturer": {
                "id": 98,
                "name": "MANN-HUMMEL",
                "slug": "mann-hummel",
                "code": "MAN98"
            },
            "manufacturer_no": "HU 816 z KIT",
            "car_brand": {
                "id": 5,
                "name": "BMW",
                "slug": "bmw",
                "code": "BMW5"
            },
            "supplier": {
                "user": 2,
                "company_name": "Mercanlar",
                "supplier_slug": "mercanlar",
                "code": "MERC"
            },
            "image": null,
            "product_image_url": null,
            "image_path": "/images/autopart/Manufacturer/MANN-HUMMEL.png",
            "moq": null,
            "currency": {
                "id": 2,
                "currency_code": "EUR",
                "currency_name": "Euro",
                "currency_symbol": "€"
            },
            "currency_price": 10.34,
            "supplier_net_price": 122.87,
            "price_net": 135.16,
            "supplier_iskonto": "%40"
        }
    ]
}

```
***
**endpoint:** api/autopart/brands/

**method:** GET

**serializer:** CarBrandListSerializer

**view:** CarBrandListAPIView


## JSON
```
{
    "count": 82,
    "next": "http://127.0.0.1:8000/api/autopart/brands/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "ALFA ROMEO",
            "slug": "alfa-romeo",
            "code": "ALF1",
            "image": "http://127.0.0.1:8000/images/autopart/CarBrand/ALFA%20ROMEO.png"
        },
        {
            "id": 2,
            "name": "ASTON MARTIN",
            "slug": "aston-martin",
            "code": "AST2",
            "image": "http://127.0.0.1:8000/images/autopart/default.png"
        }
    ]
}

```
***
**endpoint:** api/autopart/brand/<slug>/

**method:** GET

**serializer:** CarBrandDetailSerializer

**view:** CarBrandDetailAPIView


## JSON
```
{
    "id": 3,
    "name": "AUDI",
    "slug": "audi",
    "code": "AUD3",
    "image": "http://127.0.0.1:8000/images/autopart/CarBrand/AUDI.png",
    "description": null,
    "products": [
        {
            "id": 1,
            "name": "AUDI ERA 06A919501A",
            "oem_code": "06A919501A",
            "sku": "MERC-AUD3-ERA43-06A919501A",
            "upc": null,
            "slug": "audi-era-06a919501a-merc-aud3-era43-06a919501a",
            "manufacturer": {
                "id": 43,
                "name": "ERA",
                "slug": "era",
                "code": "ERA43"
            },
            "manufacturer_no": "E-330546",
            "car_brand": {
                "id": 3,
                "name": "AUDI",
                "slug": "audi",
                "code": "AUD3"
            },
            "supplier": {
                "user": 2,
                "company_name": "Mercanlar",
                "supplier_slug": "mercanlar",
                "code": "MERC"
            },
            "image": null,
            "product_image_url": null,
            "image_path": "/images/autopart/default.png",
            "moq": null,
            "currency": {
                "id": 2,
                "currency_code": "EUR",
                "currency_name": "Euro",
                "currency_symbol": "€"
            },
            "currency_price": 4.34,
            "supplier_net_price": 71.04,
            "price_net": 78.14,
            "supplier_iskonto": "%20+5"
        }
    ]
}
```