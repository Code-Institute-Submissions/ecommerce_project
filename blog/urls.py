from django.conf.urls import url
from .views import getposts, viewpost, addcomment

urlpatterns = [
    url(r'^$', getposts,  name='getposts'),
    url(r'^posts/(\d+)$', viewpost,  name='viewpost'),
    url(r'^posts/(.+)/comments/add$', addcomment,  name='addcomment'),
]