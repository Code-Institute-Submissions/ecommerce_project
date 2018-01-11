from django.contrib import admin
from .models import Product, Category
from mptt.admin import MPTTModelAdmin

# Register your models here.

admin.site.register(Product)

admin.site.register(Category , MPTTModelAdmin) 

