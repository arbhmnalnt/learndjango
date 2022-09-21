import datetime
from django.utils.timezone import now

from django.db import models

# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True

class Product(TimeStampMixin,models.Model):
    name        = models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price       = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="",blank=True)
    department = models.CharField(max_length=100)
    createdTime = models.DateTimeField(auto_now_add=True, null=True,verbose_name = "time created")
    lastTimeupdated = models.DateTimeField(auto_now=True, null=True,verbose_name = "last time modified")

class ProductImage(TimeStampMixin,models.Model):
    image   = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    description = models.TextField(default="",blank=True)

