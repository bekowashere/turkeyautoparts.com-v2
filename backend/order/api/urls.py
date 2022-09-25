from django.urls import path
from order.api.views import (
    OrderListAPIView,
    OrderDetailAPIView,
    OrderItemDetailAPIView,
    OrderCreateAPIView,
    # CUSTOMER
    CustomerOrderListAPIView,
    CustomerOrderDetailAPIView,
    # SUPPLIER
    SupplierSubOrderListAPIView,
    SupplierSubOrderDetailAPIView
)

app_name = 'order'

urlpatterns = [
    # SUPERUSER - ADMIN
    path('list/', OrderListAPIView.as_view(), name='order_list'),
    path('detail/<order_key>/', OrderDetailAPIView.as_view(), name='order_detail'),

    # CUSTOMER
    path('customer/list/', CustomerOrderListAPIView.as_view(), name='customer_order_list'),
    path('customer/detail/<order_key>/', CustomerOrderDetailAPIView.as_view(), name='customer_order_detail'),

    # SUPPLIER
    path('supplier/list/', SupplierSubOrderListAPIView.as_view(), name='supplier_order_list'),
    path('supplier/detail/<suborder_key>/', SupplierSubOrderDetailAPIView.as_view(), name='supplier_order_detail'),

    # CREATE
    path('create/', OrderCreateAPIView.as_view(), name='order_create'),

    #
    path('item/detail/<item_key>/', OrderItemDetailAPIView.as_view(), name='item_detail'),

]