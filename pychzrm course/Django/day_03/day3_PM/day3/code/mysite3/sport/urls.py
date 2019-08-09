

# file: sport/urls.py

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^templates$', views.index_view),
]

