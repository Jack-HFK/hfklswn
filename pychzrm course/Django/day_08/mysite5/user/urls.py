from django.conf.urls import url
from . import views
# file:user/urls.py

urlpatterns = [
    url(r"^login$", views.login_view),
    url(r"^logout$", views.logout_view),
    url(r"^reg2/$", views.reg2_view),
    url(r"^reg$",views.reg_view),

]