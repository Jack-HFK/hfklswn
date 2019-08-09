"""
file:tokens/urls.py
"""
from django.conf.urls import url

from tokens import views

urlpatterns = [
    url(r"^$",views.tokens_view,name="tokens"),

]
