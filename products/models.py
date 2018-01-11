from __future__ import unicode_literals
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

# Create your models here.

class Product(models.Model):
    category = TreeManyToManyField('Category')
    product_name = models.CharField(max_length=254, default='')
    search_price = models.DecimalField(max_digits=6, decimal_places=2)
    aw_image_url = models.CharField(max_length=500, default='')
    merchant_deep_link = models.CharField(max_length=500, default='')
    slug = models.SlugField(default='product')
    
    def __str__(self):
        return self.product_name
        
class Category(MPTTModel):
	name = models.CharField(max_length=50, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
	slug = models.SlugField()
	
	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		unique_together = (('parent', 'slug',))
		verbose_name_plural = 'categories'
		
	def get_slug_list(self):
		try:
			ancestors = self.get_ancestors(include_self=True)
		except:
			ancestors = []
		else:
			ancestors = [ i.slug for i in ancestors]
		slugs = []
		for i in range(len(ancestors)):
			slugs.append('/'.join(ancestors[:i+1]))
		return slugs
		
	def __str__(self):
		return self.name
	
        



