from django.contrib import admin

from .models import Product, Amount, Log, Brand, Category

admin.site.register([Amount, Log, Brand, Category])

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