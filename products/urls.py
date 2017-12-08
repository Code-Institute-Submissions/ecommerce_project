from django.conf.urls import url
from .views import viewproducts, do_search, show_category

urlpatterns = [
 url(r'^$', viewproducts, name='viewproducts'),
 url(r'^search/', do_search, name='search'),
 url(r'^category/(?P<hierarchy>.+)/$', show_category, name='category'),
 
]
