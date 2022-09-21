from django.contrib import admin
from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastTimeupdated','createdTime', 'created_at')

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product','created_at','updated_at')
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)