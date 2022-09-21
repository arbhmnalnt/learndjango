from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastTimeupdated','createdTime')
# Register your models here.
admin.site.register(Product, ProductAdmin)