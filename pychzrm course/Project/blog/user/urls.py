from django.conf.urls import url
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/vi/users
    url(r"^$", views.users_view, name="users"),
    url(r"^/(?P<username>[\w]+)$",views.users_view),
    url(r"^/(?P<username>[\w]+)/avatar$",views.user_avatar_view),
]


