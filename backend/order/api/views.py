# Rest Framework Views
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

# Rest Framework Helpers
from rest_framework.response import Response
from rest_framework import status

# FILTERS
from django_filters.rest_framework import DjangoFilterBackend

# PERMISSIONS
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from order.models import OrderItem, Order, SubOrder
from order.api.serializers import (
    OrderItemDetailSerializer,
    OrderDetailSerializer,
    OrderListSerializer,
    CustomerOrderDetailSerializer,
    SupplierSubOrderListSerializer,
    SupplierSubOrderDetailSerializer
)

from account.models import CustomerUser, Address, SupplierUser
from autopart.models import Product

from django.utils.crypto import get_random_string


# ORDER ITEM
class OrderItemDetailAPIView(RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemDetailSerializer
    lookup_field = 'item_key'

# ! ORDER
# * SUPER USER
class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_delivered', 'status']
    # search field = username ve order_key ekle

class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = 'order_key'

# * CUSTOMER
class CustomerOrderListAPIView(ListAPIView):
    serializer_class = OrderListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_delivered', 'shipping_address']

    def get_queryset(self):
        user = self.request.user
        customer = CustomerUser.objects.get(user=user)
        orders = Order.objects.filter(user=customer)
        return orders
    
class CustomerOrderDetailAPIView(RetrieveAPIView):
    serializer_class = CustomerOrderDetailSerializer
    # permission_classes =[]
    lookup_field = 'order_key'

    def get_queryset(self):
        user = self.request.user
        customer = CustomerUser.objects.get(user=user)
        orders = Order.objects.filter(user=customer)
        return orders

# * SUPPLIER
class SupplierSubOrderListAPIView(ListAPIView):
    serializer_class = SupplierSubOrderListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sub_order_status', 'sub_status']

    def get_queryset(self):
        user = self.request.user
        supplier = SupplierUser.objects.get(user=user)
        orders = SubOrder.objects.filter(supplier=supplier)
        return orders

class SupplierSubOrderDetailAPIView(RetrieveAPIView):
    serializer_class = SupplierSubOrderDetailSerializer
    # permission_classes =[]
    lookup_field = 'suborder_key'

    def get_queryset(self):
        user = self.request.user
        supplier = SupplierUser.objects.get(user=user)
        orders = SubOrder.objects.filter(supplier=supplier)
        return orders

class OrderCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        user = request.user
        
        is_paid = data.get('is_paid')
        payment_method = data.get('payment_method')
        total_price = data.get('total_price')

        shipping_address = data.get('shipping_address')
        shipping_method = data.get('shipping_method')
        shipping_price = data.get('shipping_price')

        # GET OBJECT
        customerUser = CustomerUser.objects.get(user=user)
        address = Address.objects.get(id=shipping_address)

        # CREATE UNIQUE ORDER KEY
        iso2 = address.country.iso2
        ex = False
        new_order_key = f'{iso2}-{get_random_string(9, "0123456789")}'
        ex = Order.objects.filter(order_key=new_order_key).exists()
        while ex:
            new_order_key = f'{iso2}-{get_random_string(9, "0123456789")}'
            ex = Order.objects.filter(order_key=new_order_key).exists()

        order_key = new_order_key

        try:
            order = Order.objects.create(
                user=customerUser,
                order_key=order_key,
                is_paid=is_paid,
                payment_method=payment_method,
                total_price=total_price,
                shipping_address=address,
                shipping_method=shipping_method,
                shipping_price=shipping_price
            )

            
            #  "suppliers_code": ["MERC", "DNMK"]
            suppliers_code = data.pop('suppliers_code')
            # CREATE SUBORDER
            for _code in suppliers_code:
                suborder_key = f'{_code}-{order_key}'
                try:
                    suborder = SubOrder.objects.get(suborder_key=suborder_key)
                except:
                    supplier = SupplierUser.objects.get(code=_code)
                    suborder = SubOrder(
                        suborder_key=suborder_key,
                        order=order,
                        supplier=supplier
                    )
                    suborder.save()


            items = data.pop('cartItems')

            for item in items:
                product_id = item.get('id')
                product = Product.objects.get(id=product_id)

                supplier_code = item.get('supplier_code')
                suborder_key = f'{supplier_code}-{order_key}'
                suborder = SubOrder.objects.get(suborder_key=suborder_key)

                quantity = item.get('quantity')
                price_net = item.get('price_net')
                price = quantity * price_net

                # CREATE UNIQUE ITEM KEY
                ex = False
                new_item_key = f'{order_key}-{get_random_string(9, "0123456789")}'
                ex = OrderItem.objects.filter(item_key=new_item_key).exists()
                while ex:
                    new_item_key = f'{order_key}-{get_random_string(9, "0123456789")}'
                    ex = OrderItem.objects.filter(item_key=new_item_key).exists()

                item_key = new_item_key

                OrderItem.objects.create(
                    item_key=item_key,
                    order=order,
                    sub_order=suborder,
                    product=product,
                    quantity=quantity,
                    price=price
                )

        except Exception as e:
            print(e)
            return Response({'status':'error', 'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'success', 'detail': 'Order created successfully'}, status=status.HTTP_200_OK)