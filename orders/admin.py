from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Order, OrderItem


def order_detail(obj):
    return mark_safe('<a href="{}">Обзор</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id])
    ))


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created',
                    'updated', order_detail]
    list_filter = ['paid', 'created', 'updated', ]
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


