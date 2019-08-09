"""mywebsite1 URL Configuration

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
from .import views  #相对导入：当前文件夹相对导入文件夹


#该文件会包含 urlpatterns 的列表用于表示路由 - 视图映射 , 通过 url() 表示具体映射
# 主路由映射文件
urlpatterns = [
# URL匹配规则：自上而下依次匹配查找路由和url()函数
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.index_view),
    url(r"^page1$", views.page1_view),
    url(r"^page2$", views.page2_view),
    url(r"^page3$", views.page3_view),
    # 一个分组表示一个参数,多个参数需要使用多个分组 , 并且使用个 / 隔开
    url(r"^year/(\d{4})$", views.year_view),
    url(r"^(\d+)/(\w{3})/(\d+)$", views.cal_view),
    # /date/2008/08/08      位置传参传递给视图函数
    url(r"date/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$", views.date_viem),
    # 正则表达式给分组起名：捕获组，利用组名匹配关键字传参：实现关键字传参，路由可以不按顺序传递
    # /date/08/08/2008    views.date_view(request,m="10",d="30",y="2008")
    url(r"date/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$", views.date_viem),
    url(r'^show_info$', views.show_info_view),
    url(r"^page$", views.page_view),
    url(r"^sum$", views.sum_view),
]
