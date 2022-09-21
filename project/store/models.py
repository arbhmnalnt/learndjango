import datetime
from django.utils.timezone import now

from django.db import models

# Create your models here.

class Product(models.Model):
    name        = models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price       = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="",blank=True)
    department = models.CharField(max_length=100)
    createdTime = models.DateTimeField(auto_now_add=True, null=True,verbose_name = "time created")
    lastTimeupdated = models.DateTimeField(auto_now=True, null=True,verbose_name = "last time modified")
