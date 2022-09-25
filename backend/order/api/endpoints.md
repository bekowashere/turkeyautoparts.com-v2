# order API endpoints
***
**endpoint:** api/order/list/

**method:** GET

**serializer:** OrderListSerializer

**view:** OrderListAPIView

**filterset_fields:** ['is_delivered', 'status']


## JSON
```
[
    {
        "id": 1,
        "order_key": "TR-123456789",
        "user": {
            "username": "c-berkekaratas",
            "email": "customer@gmail.com",
            "first_name": "Berke",
            "last_name": "Karataş"
        },
        "total_price": 500.0,
        "is_delivered": true,
        "shipping_address": {
            "id": "b7f8b7d0-92c3-46aa-87ec-9da41da12382",
            "country": {
                "id": 228,
                "iso2": "TR",
                "name": "Turkey",
                "region": "Asia"
            },
            "address_name": "Home",
            "first_name": "Berke",
            "last_name": "Karataş",
            "company_name": null,
            "phone_number": null,
            "street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",
            "street_address_2": null,
            "postal_code": "34055",
            "city": "Eyupsultan",
            "city_area": "Istanbul",
            "user": 3
        },
        "shipping_method": 0
    }
]
```
***

**endpoint:** api/order/detail/<order_key>/

**method:** GET

**serializer:** OrderDetailSerializer

**view:** OrderDetailAPIView


## JSON
```
{
    "id": 1,
    "order_key": "TR-123456789",
    "user": {
        "username": "c-berkekaratas",
        "email": "customer@gmail.com",
        "first_name": "Berke",
        "last_name": "Karataş"
    },
    "is_paid": true,
    "paid_date": "2022-09-22T12:22:07Z",
    "payment_method": "Bank Account",
    "total_price": 500.0,
    "is_delivered": true,
    "delivered_date": "2022-09-22T12:22:15Z",
    "shipping_address": {
        "id": "b7f8b7d0-92c3-46aa-87ec-9da41da12382",
        "country": {
            "id": 228,
            "iso2": "TR",
            "name": "Turkey",
            "region": "Asia"
        },
        "address_name": "Home",
        "first_name": "Berke",
        "last_name": "Karataş",
        "company_name": null,
        "phone_number": null,
        "street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",
        "street_address_2": null,
        "postal_code": "34055",
        "city": "Eyupsultan",
        "city_area": "Istanbul",
        "user": 3
    },
    "shipping_method": 0,
    "shipping_price": 10.0,
    "tracking_number": null,
    "sub_orders": [
        {
            "id": 1,
            "suborder_key": "MERC-TR-123456789",
            "supplier": {
                "username": "mercanlar",
                "email": "mercanlar@gmail.com",
                "company_name": "Mercanlar",
                "supplier_slug": "mercanlar",
                "code": "MERC",
                "company_image": "/images/account/suppliers/default.png"
            },
            "sub_total_price": 200.0,
            "order_items": [
                {
                    "id": 1,
                    "item_key": "TR-123456789-123856921",
                    "product": {
                        "id": 1,
                        "name": "AUDI ERA 06A919501A",
                        "oem_code": "06A919501A",
                        "slug": "merc-aud3-era43-06a919501a",
                        "sku": "MERC-AUD3-ERA43-06A919501A",
                        "price_net": 78.14
                    },
                    "quantity": 5,
                    "price": 100.0
                },
                {
                    "id": 2,
                    "item_key": "TR-123456789-546852179",
                    "product": {
                        "id": 3,
                        "name": "AUDI ERA 06A906433L",
                        "oem_code": "06A906433L",
                        "slug": "merc-aud3-era43-06a906433l",
                        "sku": "MERC-AUD3-ERA43-06A906433L",
                        "price_net": 153.49
                    },
                    "quantity": 10,
                    "price": 300.0
                }
            ]
        }
    ],
    "created_date": "2022-09-22T12:22:17.205021Z",
    "updated_date": "2022-09-22T12:22:17.205021Z",
    "order_items": [
        {
            "id": 1,
            "item_key": "TR-123456789-123856921",
            "product": {
                "id": 1,
                "name": "AUDI ERA 06A919501A",
                "oem_code": "06A919501A",
                "slug": "merc-aud3-era43-06a919501a",
                "sku": "MERC-AUD3-ERA43-06A919501A",
                "price_net": 78.14
            },
            "quantity": 5,
            "price": 100.0
        },
        {
            "id": 2,
            "item_key": "TR-123456789-546852179",
            "product": {
                "id": 3,
                "name": "AUDI ERA 06A906433L",
                "oem_code": "06A906433L",
                "slug": "merc-aud3-era43-06a906433l",
                "sku": "MERC-AUD3-ERA43-06A906433L",
                "price_net": 153.49
            },
            "quantity": 10,
            "price": 300.0
        }
    ]
}
```
***

**endpoint:** api/order/customer/list/

**method:** GET

**serializer:** OrderListSerializer

**view:** CustomerOrderListAPIView


## JSON
```
[
    {
        "id": 1,
        "order_key": "TR-123456789",
        "user": {
            "username": "c-berkekaratas",
            "email": "customer@gmail.com",
            "first_name": "Berke",
            "last_name": "Karataş"
        },
        "total_price": 500.0,
        "is_delivered": true,
        "shipping_address": {
            "id": "b7f8b7d0-92c3-46aa-87ec-9da41da12382",
            "country": {
                "id": 228,
                "iso2": "TR",
                "name": "Turkey",
                "region": "Asia"
            },
            "address_name": "Home",
            "first_name": "Berke",
            "last_name": "Karataş",
            "company_name": null,
            "phone_number": null,
            "street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",
            "street_address_2": null,
            "postal_code": "34055",
            "city": "Eyupsultan",
            "city_area": "Istanbul",
            "user": 3
        },
        "shipping_method": 0
    }
]
```
***

**endpoint:** api/order/customer/detail/<order_key>/

**method:** GET

**serializer:** CustomerOrderDetailSerializer

**view:** CustomerOrderDetailAPIView


## JSON
```
{
    "id": 1,
    "order_key": "TR-123456789",
    "is_paid": true,
    "paid_date": "2022-09-22T12:22:07Z",
    "payment_method": "Bank Account",
    "total_price": 500.0,
    "is_delivered": true,
    "delivered_date": "2022-09-22T12:22:15Z",
    "shipping_address": {
        "id": "b7f8b7d0-92c3-46aa-87ec-9da41da12382",
        "country": {
            "id": 228,
            "iso2": "TR",
            "name": "Turkey",
            "region": "Asia"
        },
        "address_name": "Home",
        "first_name": "Berke",
        "last_name": "Karataş",
        "company_name": null,
        "phone_number": null,
        "street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",
        "street_address_2": null,
        "postal_code": "34055",
        "city": "Eyupsultan",
        "city_area": "Istanbul",
        "user": 3
    },
    "shipping_method": 0,
    "shipping_price": 10.0,
    "tracking_number": null,
    "order_items": [
        {
            "id": 1,
            "item_key": "TR-123456789-123856921",
            "product": {
                "id": 1,
                "name": "AUDI ERA 06A919501A",
                "oem_code": "06A919501A",
                "slug": "merc-aud3-era43-06a919501a",
                "sku": "MERC-AUD3-ERA43-06A919501A",
                "price_net": 78.14
            },
            "quantity": 5,
            "price": 100.0
        },
        {
            "id": 2,
            "item_key": "TR-123456789-546852179",
            "product": {
                "id": 3,
                "name": "AUDI ERA 06A906433L",
                "oem_code": "06A906433L",
                "slug": "merc-aud3-era43-06a906433l",
                "sku": "MERC-AUD3-ERA43-06A906433L",
                "price_net": 153.49
            },
            "quantity": 10,
            "price": 300.0
        }
    ]
}
```
***

**endpoint:** api/order/supplier/list/

**method:** GET

**serializer:** SupplierSubOrderListSerializer

**view:** SupplierSubOrderListAPIView


## JSON
```
[
    {
        "id": 1,
        "order_key": "TR-123456789",
        "suborder_key": "MERC-TR-123456789",
        "sub_total_price": 200.0,
        "sub_order_status": 0,
        "sub_status": 0
    }
]
```
***

**endpoint:** api/order/supplier/detail/<suborder_key>/

**method:** GET

**serializer:** SupplierSubOrderDetailSerializer

**view:** SupplierSubOrderDetailAPIView


## JSON
```
...
{
    "id": 1,
    "order_key": "TR-123456789",
    "suborder_key": "MERC-TR-123456789",
    "sub_total_price": 200.0,
    "sub_order_status": 0,
    "sub_status": 0,
    "order_items": [
        {
            "id": 1,
            "item_key": "TR-123456789-123856921",
            "product": {
                "id": 1,
                "name": "AUDI ERA 06A919501A",
                "oem_code": "06A919501A",
                "slug": "merc-aud3-era43-06a919501a",
                "sku": "MERC-AUD3-ERA43-06A919501A",
                "price_net": 78.14
            },
            "quantity": 5,
            "price": 100.0
        },
        {
            "id": 2,
            "item_key": "TR-123456789-546852179",
            "product": {
                "id": 3,
                "name": "AUDI ERA 06A906433L",
                "oem_code": "06A906433L",
                "slug": "merc-aud3-era43-06a906433l",
                "sku": "MERC-AUD3-ERA43-06A906433L",
                "price_net": 153.49
            },
            "quantity": 10,
            "price": 300.0
        }
    ]
}
***

**endpoint:** api/order/create/

**method:** POST

**view:** OrderCreateAPIView


## Fields
```
{
    "is_paid": true,
    "payment_method": "Credit Card",
    "total_price": 155.50,
    "shipping_address": "b7f8b7d0-92c3-46aa-87ec-9da41da12382",
    "shipping_method": 0,
    "shipping_price": 10,
    "suppliers_code": ["MERC"],
    "cartItems": [
        {
            "id":87,
            "name":"BMW MANN-HUMMEL 11427837997",
            "price_net": 211.22,
            "quantity": 4,
            "supplier_code": "MERC"
        },
        {
            "id":85,
            "name":"BMW MANN-HUMMEL 13717630911",
            "price_net": 206.78,
            "quantity": 1,
            "supplier_code": "MERC"
        }
    ]
}
```

## JSON
```
{
    'status':'success',
    'detail': 'Order created successfully'
}
```