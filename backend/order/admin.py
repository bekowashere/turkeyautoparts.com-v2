from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from order.models import OrderItem, Order, SubOrder

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Order Information'), {'fields': ('user', 'order_key')}),
        (_('Payment Information'), {'fields': ('payment_method', 'total_price', 'is_paid', 'paid_date')}),
        (_('Tracking Information'), {'fields': ('tracking_number',)}),
        (_('Shipping Information'), {'fields': ('shipping_address', 'shipping_method', 'shipping_price', 'is_delivered', 'delivered_date')}),
        (_('Metadata Information'), {'fields': ('created_date', 'updated_date')}),
    )

    list_display = ('order_key', 'user', 'tracking_number', 'is_paid', 'is_delivered')
    # LOOK: payment_method & shipping_method options --> add list_filter
    list_filter = ('is_paid', 'is_delivered')
    search_fields = ('user__user__email', 'order_key', 'tracking_number')
    readonly_fields = ('created_date', 'updated_date')

    inlines = [
        OrderItemInline
    ]

admin.site.register(SubOrder)
admin.site.register(OrderItem)

