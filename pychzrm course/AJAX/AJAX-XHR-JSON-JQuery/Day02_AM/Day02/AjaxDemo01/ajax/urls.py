from django.conf.urls import url
from . import views

urlpatterns = [
  # 1. 演示创建xhr
  url(r'^01-createxhr/$', views.create_views),
  # 2. 演示使用ajax发送get请求的步骤
  url(r'^02-server/$', views.server02_views),
  url(r'^02-ajax-get/$', views.ajaxget_views),
  # 3. 演示使用ajax发送get请求并附带参数
  url(r'^03-ajax-get-params/$', views.getparams_views),
  url(r'^03-server/$', views.server03_views),
  # 4. 使用 AJAX 完成注册操作
  url(r'^04-register/$',views.register_views),
  url(r'^04-checkuname/$',views.checkuname_views),
  url(r'^04-reguser/$',views.reguser_views),
  url(r'^04-regpost/$',views.regpost_views),
  # 5. 使用AJAX发送post请求
  url(r'^05-ajax-post/$',views.post_views),
  url(r'^05-server/$',views.server05_views),
]











