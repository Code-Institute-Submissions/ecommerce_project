from django.conf.urls import url
from .views import viewed, add_to_viewed

urlpatterns = [
    url(r'^$', viewed, name='viewed'),
    url(r'^add/(?P<id>\d+)', add_to_viewed, name='add_to_viewed'),
]