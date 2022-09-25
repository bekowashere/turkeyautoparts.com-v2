# ACCOUNT

### - Together

:x: **email**

:x: **password**


### - Customer

:heavy_check_mark: **[POST]** `api/token/`

:heavy_check_mark: **[POST]** `api/login/customer/`

:heavy_check_mark: **[POST]** `api/account/register/customer/`

:heavy_check_mark: **[PUT]** `api/account/customer/update/information/`

:heavy_check_mark: **[PUT]** `api/account/customer/update/default-address/`

:heavy_check_mark: **[GET]** `api/account/customer/<username>`

:heavy_check_mark: **[POST PUT DELETE]** `api/account/customer/change/address/`


### - Supplier

:heavy_check_mark: **[POST]** `api/token/`

:heavy_check_mark: **[POST]** `api/login/supplier/`

:heavy_check_mark: **[POST]** `api/account/register/supplier/`

:heavy_check_mark: **[GET]** `api/account/supplier/<username>`

:heavy_check_mark: **[PUT]** `api/account/supplier/update/username/`

:heavy_check_mark: **[PUT]** `api/account/supplier/update/information/`

:heavy_check_mark: **[PUT]** `api/account/supplier/update/address/`

:heavy_check_mark: **[PUT]** `api/account/supplier/update/image/`

___


# AUTO

:heavy_check_mark: **[GET]** `api/auto/brands/`

:heavy_check_mark: **[GET]** `api/auto/brands/detail/<brand_slug>`

:heavy_check_mark: **[GET]** `api/auto/series/`

:heavy_check_mark: **[GET]** `api/auto/series/detail/<series_slug>`

:heavy_check_mark: **[GET]** `api/auto/models/`

:heavy_check_mark: **[GET]** `api/auto/models/detail/<model_slug>`

:heavy_check_mark: **[GET]** `api/auto/cars/detail/<car_slug>`

___


# AUTOPART

:heavy_check_mark: **[GET]** `api/autopart/products/`

:heavy_check_mark: **[GET]** `api/autopart/product/<slug>`

:heavy_check_mark: **[GET]** `api/autopart/manufacturers/`

:heavy_check_mark: **[GET]** `api/autopart/manufacturer/<slug>`

:heavy_check_mark: **[GET]** `api/autopart/brands/`

:heavy_check_mark: **[GET]** `api/autopart/brand/<slug>`

___


# ORDER

:heavy_check_mark: **[POST]** `api/order/create/`

:heavy_check_mark: **[GET]** `api/order/list/`

:heavy_check_mark: **[GET]** `api/order/detail/<order_key>/`

:heavy_check_mark: **[GET]** `api/order/customer/list/`

:heavy_check_mark: **[GET]** `api/order/customer/detail/<order_key>/`

:heavy_check_mark: **[GET]** `api/order/supplier/list/`

:heavy_check_mark: **[GET]** `api/order/supplier/detail/<suborder_key>/`
___

# GLOSSARY

:heavy_check_mark: **[GET]** `api/glossary/list/`

:heavy_check_mark: **[GET]** `api/glossary/detail/<slug>/`
___

# NEWS

:heavy_check_mark: **[GET]** `api/news/list/`

:heavy_check_mark: **[GET]** `api/news/detail/<slug>/`
