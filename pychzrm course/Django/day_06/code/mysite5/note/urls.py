from django.conf.urls import url

from . import views

urlpatterns = [

    url(r"^add$", views.add_view),  # 增
    url(r"^$", views.list_view),  # 查
    url(r"^del/(\d+)", views.del_view),  # 删
    url(r"^mod/(\d+)", views.mod_view),  # 改

]
