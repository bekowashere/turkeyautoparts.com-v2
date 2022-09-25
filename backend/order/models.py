from django.db import models
from account.models import CustomerUser, SupplierUser, Address
from autopart.models import Product
from django.utils.translation import gettext_lazy as _

"""
kayıtlı, devam eden siparişler ve tamamlanan siparişler --> is_saved
shipping_method ?
tracking_number --> Tracking model?
"""
class Order(models.Model):
    LAND = 0
    AIR = 1
    SEA = 2

    SHIPPING_METHODS = (
        (LAND, 'Land Transport'),
        (AIR, 'Air Transport'),
        (SEA, 'Sea Transport'),
    )

    OPEN = 0
    CLOSED = 1
    
    STATUS = (
        (OPEN, 'OPEN'),
        (CLOSED, 'CLOSED'),
    )

    user = models.ForeignKey(
        CustomerUser,
        on_delete=models.CASCADE,
        related_name="user_orders",
        verbose_name=_('Customer')
    )
    order_key = models.CharField(_('Order Key'), max_length=128)
    # order_name = models.CharField(_('Order Name'), max_length=128)
    # is_saved = models.BooleanField(_('Saved Order'), default=False)

    # Payment
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)
    # LOOK: method options
    payment_method = models.CharField(_('Payment Method'),max_length=32)
    total_price = models.DecimalField(
        _('Total Price'),
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True
    )

    # Shipping
    is_delivered = models.BooleanField(default=False)
    delivered_date = models.DateTimeField(null=True, blank=True)

    shipping_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Shipping Address')
    )
    shipping_method = models.IntegerField(_('Shipping Method'), default=LAND, choices=SHIPPING_METHODS)
    shipping_price = models.DecimalField(
        _('Shipping Price'),
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True
    )

    tracking_number = models.CharField(
        _('Tracking Number'),
        max_length=128,
        null=True,
        blank=True
    )

    status = models.IntegerField(_('Sub Status'), default=OPEN, choices=STATUS)

    # Metadata
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now=True)

    @property
    def get_all_items(self):
        return self.items.all()

    @property
    def get_all_sub_orders(self):
        return self.sub_orders.all()

    def __str__(self):
        return self.order_key

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class SubOrder(models.Model):
    # order_status
    TAKEN = 0
    PREPARING = 1
    SEND = 2

    SUB_ORDER_STATUS = (
        (TAKEN, 'Sipariş Alındı'),
        (PREPARING, 'Hazırlanıyor'),
        (SEND, 'Kargoya Verildi'),
    )

    # status
    OPEN = 0
    CLOSED = 1
    
    SUB_STATUS = (
        (OPEN, 'OPEN'),
        (CLOSED, 'CLOSED'),
    )

    suborder_key = models.CharField(_('Sub Order Key'), max_length=128, null=True, blank=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="sub_orders",
        verbose_name=_('Order')
    )
    supplier = models.ForeignKey(
        SupplierUser,
        on_delete=models.CASCADE,
        related_name="supplier_sub_orders",
        verbose_name=_('Supplier')
    )
    sub_total_price = models.DecimalField(
        _('Total Price'),
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True
    )

    sub_order_status = models.IntegerField(_('Sub Order Status'), default=TAKEN, choices=SUB_ORDER_STATUS)
    is_received = models.BooleanField(_('Received'), default=False, help_text='Received by us')
    sub_status = models.IntegerField(_('Sub Status'), default=OPEN, choices=SUB_STATUS)


    @property
    def get_all_items(self):
        return self.sub_items.all()

    def __str__(self):
        return self.suborder_key

    class Meta:
        verbose_name = _('Sub Order')
        verbose_name_plural = _('Sub Orders')


class OrderItem(models.Model):
    item_key = models.CharField(_('Item Key'), max_length=128, null=True, blank=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_('Order')
    )
    sub_order = models.ForeignKey(
        SubOrder,
        on_delete=models.CASCADE,
        related_name="sub_items",
        verbose_name=_('Sub Order')
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_order_items",
        verbose_name=_('Product')
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=1,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        _('Price'),
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.item_key

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')