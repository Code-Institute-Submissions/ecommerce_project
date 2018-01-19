from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import viewproducts
from .models import Product

class TestViewProducts(TestCase):
    def test_viewproducts_resolves(self):
        page = resolve('/products/')
        self.assertEqual(page.func, viewproducts)
        
