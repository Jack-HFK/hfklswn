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
  # 6. 使用AJAX读取数据
  url(r'^06-ajax-users/$',views.users_views),
  url(r'^06-server/$',views.server06_views),
  # 7. 在前端中处理JSON格式字符串
  url(r'^07-json/$',views.json_views),
  # 8. 在服务器端中处理JSON字符串
  url(r'^08-json-server/$',views.jsonserver_views),
  # 9. 在服务器端中,读取Users表中的数据再转换成JSON串
  url(r'^09-json-users/$',views.jsonusers_views),
  # 10. 读取Users信息并显示在网页上(使用JSON)
  url(r'^10-users/$',views.jsonusers_views),
  url(r'^10-server/$',views.server10_views),
  # 11. 前端中将JS对象转换成JSON串
  url(r'^11-front-json/$',views.front_views),
  url(r'^11-server-json/$',views.serverjson_views),
  # 12. 通过JSON完成注册操作
  url(r'^12-register-json/$',views.regjson_views),
  url(r'^12-server/$',views.server12_views),
  # 13. 演示jquery中的$obj.load() 的作用
  url(r'^13-head/$',views.head_views),
  url(r'^13-index/$',views.index_views),
  # 14. 演示jquery中的$.get()的作用
  url(r'^14-jq-get/$',views.jqget_views),
  # 15. 通过$.get()完成搜索建议
  url(r'^15-search/$',views.search_views),
  url(r'^15-server/$',views.server15_views),
  # 16. 通过$.ajax() 完成自定义的ajax请求
  url(r'^16-jq-ajax/$',views.jqajax_views),
]











