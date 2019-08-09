from django.conf.urls import url
from . import views


urlpatterns = [
    # post请求 注册地址
    # http://127.0.0.1:8000/v1/users
    url(r"^$",views.register_view),
    # http://127.0.0.1:8000/v1/users/<username>
    url(r"^/(?P<username>[\w]+)$",views.username_view),
]