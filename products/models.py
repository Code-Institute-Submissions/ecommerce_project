from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=254, default='')
    search_price = models.DecimalField(max_digits=6, decimal_places=2)
    aw_image_url = models.CharField(max_length=500, default='')
    aw_deep_link = models.CharField(max_length=500, default='')
    merchant_category = models.CharField(max_length=500, default='')
    category_name = models.CharField(max_length=500, default='')
    
    def __str__(self):
        return self.product_name
        



