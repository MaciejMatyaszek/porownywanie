from django.contrib import admin
from .models import *
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon',  )

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

class ProductShopAdmin(admin.ModelAdmin):
    list_display = ('product', 'shop', 'price')





admin.site.register(Product, ProductsAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(ProductShop,ProductShopAdmin)