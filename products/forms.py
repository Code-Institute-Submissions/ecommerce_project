from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       fields = ('product_name', 'description', 'search_price', 'aw_image_url')
       
    