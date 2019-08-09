"""mywebsite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^sum$",views.sum_view),
    url(r"^test_post$",views.test_pst_view),
    url(r"^test1$",views.test1_view),
    url(r"^test2$",views.test2_view),
    url(r"^test3$",views.mypage2_view),
    url(r"^page0$",views.page0_view),
    url(r"^page1$",views.page1_view),
    url(r"^page2$",views.page2_view),
    # 以下用page3 和 page/(\d+) 表示url反向解析
    url(r"page3",views.page3_view,name="page3"),
    url(r"pagen/(\d+)",views.pagen_view,name="pagen"),

]
