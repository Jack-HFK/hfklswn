"""mywebsite_bookstore URL Configuration

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
from django.conf.urls import include
from . import views

"""当 urlpatterns 内有多个url对象时,按自上而下的顺序进行配置,
一但有路由与url匹配成功,则后面的所有url被忽略,
尽量限制url正则匹配的路径,设置^$限制匹配范围"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^love/(?P<number>\d{5})/(?P<str>a{2})$", views.number_view),
    url(r"^templates1/$", views.templates1_view),
    url(r"^templates2/$", views.templates2_view),
    url(r"^templates3/$", views.templates3_view),
    url(r"^fiction_books/",include("fiction_books.urls")),
    url(r"^urlfan/(\d{5})$",views.urlfan_view,name="urlfan"),
    url(r"^create/",include("fiction_books.urls")),
    url(r"^cookie_session/",include("cookie_session.urls")),
    url(r"^forms/",include("fiction_books.urls")),
    url(r"^user/",include("user.urls")),
]
