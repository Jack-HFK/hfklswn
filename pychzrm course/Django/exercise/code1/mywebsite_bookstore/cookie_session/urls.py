from django.conf.urls import url
from . import views

# file : cookie_session/urls.py

urlpatterns = [
    url(r"^set_cookie$",views.set_cookie_view),
    url(r"^get_cookie$",views.get_cookie_view),

]
