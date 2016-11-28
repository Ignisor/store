from django.contrib import admin

from .models import Product, Amount, Log, Brand, Category, Provider, Order

admin.site.register([Amount, Brand, Category, Provider, Order])


class LogInline(admin.TabularInline):
    model = Log
    readonly_fields = ('product', 'd_amount', 'time')
    can_delete = False


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        LogInline
    ]
    search_fields = ['barcode', 'name']
    list_display = ['name', 'barcode', 'price']

admin.site.register(Product, ProductAdmin)


class LogAdmin(admin.ModelAdmin):
    list_display = ['product', 'd_amount', 'time']

admin.site.register(Log, LogAdmin)