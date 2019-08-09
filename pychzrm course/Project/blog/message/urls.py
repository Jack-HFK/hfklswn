"""
file:message/urls.py
"""
from django.conf.urls import url

from message import views

urlpatterns = [
    url(r"/(?P<topic_id>[\d]+)$",views.messages_view,name="messages")
    
] 
