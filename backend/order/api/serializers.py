from rest_framework import serializers
from order.models import OrderItem, Order, SubOrder
from account.models import Address, CustomerUser, SupplierUser
from world.models import Country
from autopart.models import Product

class UserInformationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    class Meta:
        model = CustomerUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'iso2', 'name', 'region')

class AddressSerializer(serializers.ModelSerializer):
    country = CountryDetailSerializer()

    class Meta:
        model = Address
        fields = '__all__'


# ORDER ITEM
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'oem_code', 'slug', 'sku', 'price_net')

class OrderItemDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'item_key', 'product', 'quantity', 'price')



# SUBORDER
class SupplierUserInformationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    class Meta:
        model = SupplierUser
        fields = ('username', 'email', 'company_name', 'supplier_slug', 'code', 'company_image')

class SubOrderDetailSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    supplier = SupplierUserInformationSerializer()

    def get_order_items(self, obj):
        return OrderItemDetailSerializer(obj.get_all_items, many=True).data

    class Meta:
        model = SubOrder
        fields = (
            'id',
            'suborder_key',
            'supplier',
            'sub_total_price',
            'order_items'
        )

# ORDER


# ! ADMIN (ORDER LIST [ADMIN & CUSTOMER])
"""
Admin ve CustomerUser OrderListSerializer ortak kullanabilir.
Önemli olan detay
"""
class OrderListSerializer(serializers.ModelSerializer):
    shipping_address = AddressSerializer()
    user = UserInformationSerializer()

    class Meta:
        model = Order
        fields = (
            'id',
            'order_key',
            'user',
            'total_price',
            'is_delivered',
            'shipping_address',
            'shipping_method',
            # 'tracking_number',
        )

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    sub_orders = serializers.SerializerMethodField()
    shipping_address = AddressSerializer()
    user = UserInformationSerializer()

    def get_order_items(self, obj):
        return OrderItemDetailSerializer(obj.get_all_items, many=True).data

    def get_sub_orders(self, obj):
        return SubOrderDetailSerializer(obj.get_all_sub_orders, many=True).data

    class Meta:
        model = Order
        fields = (
            'id',
            'order_key',
            'user',
            'is_paid',
            'paid_date',
            'payment_method',
            'total_price',
            'is_delivered',
            'delivered_date',
            'shipping_address',
            'shipping_method',
            'shipping_price',
            'tracking_number',
            'sub_orders',
            'created_date',
            'updated_date',
            'order_items',
        )

# ! CUSTOMER ORDER DETAIL
class CustomerOrderDetailSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    shipping_address = AddressSerializer()

    def get_order_items(self, obj):
        return OrderItemDetailSerializer(obj.get_all_items, many=True).data

    class Meta:
        model = Order
        fields = (
            'id',
            'order_key',
            'is_paid',
            'paid_date',
            'payment_method',
            'total_price',
            'is_delivered',
            'delivered_date',
            'shipping_address',
            'shipping_method',
            'shipping_price',
            'tracking_number',
            'order_items',
        )

# ! SUPPLIER ORDER
class SupplierSubOrderListSerializer(serializers.ModelSerializer):
    order_key = serializers.SerializerMethodField()

    def get_order_key(self, obj):
        return obj.order.order_key

    class Meta:
        model = SubOrder
        fields = (
            'id',
            'order_key',
            'suborder_key',
            'sub_total_price',
            'sub_order_status',
            'sub_status'
        )

class SupplierSubOrderDetailSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    order_key = serializers.SerializerMethodField()

    def get_order_key(self, obj):
        return obj.order.order_key

    def get_order_items(self, obj):
        return OrderItemDetailSerializer(obj.get_all_items, many=True).data

    def get_order_key(self, obj):
        return obj.order.order_key

    class Meta:
        model = SubOrder
        fields = (
            'id',
            'order_key',
            'suborder_key',
            'sub_total_price',
            'sub_order_status',
            'sub_status',
            'order_items'
        )