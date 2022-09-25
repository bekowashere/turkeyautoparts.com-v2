# account API endpoints
***
**endpoint:** api/token/

**method:** POST

## Fields
- **email** - string -> customer@gmail.com
- **password** - string -> Beko1234

## JSON
```
{
    "id": 2,
    "email": "customer@gmail.com",
    "first_name": "Berke",
    "last_name": "Karataş",
    "is_active": true,
    "is_customer": true,
    "is_supplier": false,
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNjE1OTM4LCJpYXQiOjE2NjI3NTE5MzgsImp0aSI6IjIwYTVkNTZjMDNjMzRkYjFiYWUyYWM4ZmZiYjViYjQzIiwidXNlcl9pZCI6Mn0.O0XHFYaeyuuUpgomrzvT5-qr6zZ3Dz9eJ7OTsc0pBzc"
}
```

> **NOTE:** The token value is important because we will use this token value to send requests (GET, POST, PUT, DELETE). 
> **KEY:** Authorization
> **VALUE:** Bearer token

***
**endpoint:** api/login/customer/

**method:** POST

## Fields

-  **email** - string -> customer@gmail.com

-  **password** - string -> Berke1919*-


## JSON

```
{

"user": 3,

"username": "customer1",

"email": "customer@gmail.com",

"first_name": "Berke",

"last_name": "Karataş",

"is_active": true,

"is_customer": true,

"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0NjM3MTE5LCJpYXQiOjE2NjM3NzMxMTksImp0aSI6IjM5YzczYTU3NWFlMjQyMjg5MmU1ZDU4Yzk1NjIyMGExIiwidXNlcl9pZCI6M30.RSTozjy6sJsnrbhvspV9fKBhA3iEtFhvAT2BVBHDD5c",

"phone_number": "+905393182715",

"note": "",

"default_shipping_address": {

"id": "8ed6ce48-b6e2-479a-90da-8d6c5b949551",

"address_name": "Home",

"country": "Turkey"

},

"addresses": [

{

"id": "8ed6ce48-b6e2-479a-90da-8d6c5b949551",

"address_name": "Home",

"first_name": "Berke",

"last_name": "Karataş",

"company_name": null,

"phone_number": "+905393182715",

"street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",

"street_address_2": null,

"postal_code": "34055",

"city": "Eyüpsultan",

"city_area": "İstanbul",

"user": 3,

"country": 228

},

{

"id": "04712657-8e40-4d15-bda4-593e9d50ed5f",

"address_name": "Home2",

"first_name": "Berke",

"last_name": "Karataş",

"company_name": "SkysSons",

"phone_number": "05322249589",

"street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",

"street_address_2": "",

"postal_code": "34055",

"city": "Eyüpsultan",

"city_area": "Istanbul",

"user": 3,

"country": 228

}

]

}
```

***
**endpoint:** api/account/register/customer/

**method:** POST

## Fields
- **email** - string -> customer@gmail.com
- **first_name** - string -> Berke
- **last_name** - string -> Karataş
- **password** - string -> Beko1234
- **password2** - string -> Beko1234

## JSON
```
{
    "status": "success",
    "user": {
        "id": 2,
        "email": "customer@gmail.com",
        "first_name": "Berke",
        "last_name": "Karataş",
        "is_active": true,
        "is_customer": true,
        "is_supplier": false,
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNjE1Mzc2LCJpYXQiOjE2NjI3NTEzNzYsImp0aSI6ImZjN2ZhM2EyMDExZjQ0NjU5MDhmYjUzOTQzZWNlNjE4IiwidXNlcl9pZCI6Mn0.MDyD8mMtDY4nkrLbPH_XysOPZphYWB699eMVszD0S14"
    }
}
```

***
**endpoint:** api/account/customer/<user__username>/

**method:** GET

## JSON
```
{
    "user": 2,
    "username": "c-berkekaratas",
    "email": "customer@gmail.com",
    "first_name": "Berke",
    "last_name": "Karataş",
    "phone_number": "",
    "default_shipping_address": null,
    "note": null
}
```

***
**endpoint:** /api/account/customer/update/information/

**method:** PUT

## Fields
- **first_name** - string -> Berke
- **last_name** - string -> Karataş
- **phone_number** - string -> +905393182715

## JSON
```
{
    "status": "success",
    "user": {
        "user": 3,
        "username": "customer1",
        "email": "customer@gmail.com",
        "first_name": "Berke",
        "last_name": "Karataş",
        "is_active": true,
        "is_customer": true,
        "phone_number": "+905393182715",
        "note": "",
        "default_shipping_address": {
            "id": "8ed6ce48-b6e2-479a-90da-8d6c5b949551",
            "address_name": "Home",
            "country": "Turkey"
        },
        "addresses": [
            {
                "id": "8ed6ce48-b6e2-479a-90da-8d6c5b949551",
                "address_name": "Home",
                "first_name": "Berke",
                "last_name": "Karataş",
                "company_name": null,
                "phone_number": "+905393182715",
                "street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",
                "street_address_2": null,
                "postal_code": "34055",
                "city": "Eyüpsultan",
                "city_area": "İstanbul",
                "user": 3,
                "country": 228
            },
            {
                "id": "04712657-8e40-4d15-bda4-593e9d50ed5f",
                "address_name": "Home2",
                "first_name": "Berke",
                "last_name": "Karataş",
                "company_name": "SkysSons",
                "phone_number": "05322249589",
                "street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",
                "street_address_2": "",
                "postal_code": "34055",
                "city": "Eyüpsultan",
                "city_area": "Istanbul",
                "user": 3,
                "country": 228
            }
        ]
    }
}
```

***
**endpoint:** /api/account/customer/update/default-address/

**method:** PUT

## Fields
- **address_id** - string -> 04712657-8e40-4d15-bda4-593e9d50ed5f


## JSON
```

```

***
**endpoint:** api/account/customer/change/address/

**method:** POST

## Fields
- **address_name** - string -> Home
- **first_name** - string -> Berke
- **last_name** - string -> Karataş
- **company_name** - string -> SkysSons
- **phone_number** - string -> 05322249589
- **street_address_1** - string -> Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10
- **street_address_2** - string -> 
- **postal_code** - string -> 34055
- **city** - string -> Eyüpsultan
- **city_area** - string -> Istanbul
- **country** - int -> 228 (Turkey)

## JSON
```
{
    "status": "success",
    "address": {
        "id": "1a76ea33-b883-48ea-a186-f0ffd52f3f2a",
        "address_name": "Home",
        "first_name": "Berke",
        "last_name": "Karataş",
        "company_name": "SkysSons",
        "phone_number": "05322249589",
        "street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",
        "street_address_2": "",
        "postal_code": "34055",
        "city": "Eyüpsultan",
        "city_area": "Istanbul",
        "user": 2,
        "country": 228
    }
}
```
**method:** PUT

## Fields
- **address_id** - string -> 1a76ea33-b883-48ea-a186-f0ffd52f3f2a
- **address_name** - string -> Home
- **first_name** - string -> Berke
- **last_name** - string -> Karataş
- **company_name** - string -> SkysSons
- **phone_number** - string -> 05322249589
- **street_address_1** - string -> Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10
- **street_address_2** - string -> 
- **postal_code** - string -> 34055
- **city** - string -> Eyüpsultan
- **city_area** - string -> Istanbul
- **country** - int -> 228 (Turkey)

## JSON
```
{
    "status": "success",
    "detail": "Address changed successfully"
}
```
**method:** DELETE

## Fields
- **address_id** - string -> 1a76ea33-b883-48ea-a186-f0ffd52f3f2a

## JSON
```
{
    "status": "success",
    "detail": "Address deleted successfully"
}
```

***
**endpoint:** api/login/supplier/

**method:** POST

  

## Fields

-  **email** - string -> mercanlar@gmail.com

-  **password** - string -> Berke1919*-

  

## JSON

```
{

"user": 2,

"email": "mercanlar@gmail.com",

"username": "mercanlar",

"is_active": true,

"is_supplier": true,

"is_verified": false,

"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0NjM3NDIwLCJpYXQiOjE2NjM3NzM0MjAsImp0aSI6ImNlNjM4NGZiMzRjNDRkMjhhNzA3NWExZGNmZTA5NGE2IiwidXNlcl9pZCI6Mn0.ESYTyDSEIVbfZy5eVRUxzxDpKH76Axrdw9oaFhfyrVY",

"company_name": "Mercanlar",

"supplier_slug": "mercanlar",

"code": "MERC",

"description": null,

"website_url": null,

"phone_number": "",

"public_phone_number": "",

"public_email": null,

"fax_number": "",

"street_address_1": "",

"street_address_2": "",

"postal_code": "",

"city": "",

"city_area": "",

"country": null,

"latitude": null,

"longitude": null,

"languages": []

}
```

***
**endpoint:** api/account/register/supplier/

**method:** POST

## Fields
- **email** - string -> supplier@gmail.com
- **password** - string -> Beko1234
- **password2** - string -> Beko1234
- **company_name** - string -> TURKEY AUTO PARTS

## JSON
```
{
    "status": "success",
    "user": {
        "id": 4,
        "email": "supplier@gmail.com",
        "username": "turkey-auto-parts",
        "company_name": "TURKEY AUTO PARTS",
        "is_active": true,
        "is_supplier": true,
        "is_verified": false,
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNjE1ODQ1LCJpYXQiOjE2NjI3NTE4NDUsImp0aSI6ImI2ZGJjYTY2ZmVkMzRkNmE4NGYwZGM4M2ZjNjhjNTU4IiwidXNlcl9pZCI6NH0.sqa-47cU8SK81BQ4TLGYIgMvlvwd-LaiawonmmzcyUw"
    }
}
```

***
**endpoint:** api/account/supplier/<user__username>/

**method:** GET


## JSON

```
{

"user": 6,

"email": "supplier3@gmail.com",

"username": "dinamik",

"is_active": true,

"is_supplier": true,

"is_verified": false,

"company_name": "Dinamik",

"supplier_slug": "dinamik",

"code": "DNMK",

"description": null,

"website_url": null,

"phone_number": "",

"public_phone_number": "",

"public_email": null,

"fax_number": "",

"street_address_1": "",

"street_address_2": "",

"postal_code": "",

"city": "",

"city_area": "",

"country": null,

"latitude": null,

"longitude": null,

"languages": []

}
```

***
**endpoint:** api/account/supplier/update/username/

**method:** PUT

## Fields
- **username** - string -> turkeyautoparts

## JSON
```
{
    "status": "success",
    "user": {
        "username": "turkeyautoparts",
        "email": "supplier@gmail.com"
    }
}
```
***
**endpoint:** api/account/supplier/update/information/

**method:** PUT

## Fields
- **company_name** - string -> TURKEY AUTO PARTS 2
- **code** - string -> TAP2
- **description** - string -> description
- **website_url** - string -> www.turkeyautoparts.com
- **public_phone_number** - string -> 02124930131
- **public_email** - string -> contact@turkeyautoparts.com
- **fax_number** - string -> 02124930131

## JSON
```
{
    "status": "success",
    "user": {
        "user": 4,
        "company_image": "/images/default.png",
        "company_name": "TURKEY AUTO PARTS 2",
        "code": "TAP2",
        "supplier_slug": "",
        "description": "description",
        "website_url": "www.turkeyautoparts.com",
        "phone_number": "",
        "public_phone_number": "02124930131",
        "public_email": "contact@turkeyautoparts.com",
        "fax_number": "02124930131",
        "street_address_1": "Topçular Mah. Cengaver Sok. No:32",
        "street_address_2": "Not",
        "postal_code": "34055",
        "city": "Eyüpsultan",
        "city_area": "Istanbul",
        "latitude": null,
        "longitude": null,
        "is_verified": false,
        "country": 228,
        "languages": []
    }
}
```
***
**endpoint:** api/account/supplier/update/address/

**method:** PUT

## Fields
- **street_address_1** - string -> Topçular Mah. Cengaver Sok. No:32
- **street_address_2** - string -> Not
- **postal_code** - string -> 34055
- **city** - string -> Eyüpsultan
- **city_area** - string -> Istanbul
- **country** - int -> 228 (Turkey)

## JSON
```
{
    "status": "success",
    "user": {
        "user": 4,
        "company_image": "/images/default.png",
        "company_name": "TURKEY AUTO PARTS 2",
        "code": "TAP2",
        "supplier_slug": "",
        "description": "description",
        "website_url": "www.turkeyautoparts.com",
        "phone_number": "",
        "public_phone_number": "02124930131",
        "public_email": "contact@turkeyautoparts.com",
        "fax_number": "02124930131",
        "street_address_1": "Topçular Mah. Cengaver Sok. No:32",
        "street_address_2": "Not",
        "postal_code": "34055",
        "city": "Eyüpsultan",
        "city_area": "Istanbul",
        "latitude": null,
        "longitude": null,
        "is_verified": false,
        "country": 228,
        "languages": []
    }
}
```
***
**endpoint:** api/account/supplier/update/image/

**method:** PUT

## Fields
- **profile_image** - FILE

## JSON
```
{
    "status": "success",
    "detail": "Profile image changed successfully"
}
```