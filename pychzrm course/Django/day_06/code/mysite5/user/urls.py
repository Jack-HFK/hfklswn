from django.conf.urls import url
from . import views
# file:user/urls.py

urlpatterns = [
    url(r"^login$", views.login_view),
    url(r"^logout$", views.logout_view)
]