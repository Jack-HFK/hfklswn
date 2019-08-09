# file :ajax/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    # １．演示创建xhr
    url(r"createxhr_01",views.create_views),
    # ２．演示使用AJAX发送请求的步骤
    url(r"^server-02/$",views.server02_views),
    url(r"^ajax-get-02/$",views.ajaxget_views),
    # ３．演示使用AJAX发送get请求并附带参数
    url(r"ajax-get-params-03/$",views.getparams_views),
    url(r"^servers-03/$",views.server03_views),
    # ４．使用AJAX完成注册操作
    url(r"^register-04/$",views.register_views),
    url(r"^checkuname-04$",views.checkunme_views),
    url(r"^reguser_04/$",views.reguser_views),
    url(r"regpost_04/",views.regpost_views),
    # 5 . 使用AJAX发送POST请求
    url(r"^ajax-post-05/$",views.post_views),
    url(r"^server-05/$",views.server05_views),
    # ６　使用AJAX读取数据
    url(r"^ajax-users-06/$",views.users_views),
    url(r"^server-06/$",views.server06_views),
    # ７　在前端中处理JSON格式字符串
    url(r"^json-07/$",views.json_views),
    # ８　在服务器端处理JSON字符串
    url(r"^json-server-08/$",views.jsonserver_views),
    # ９　在服务器端中，读取Users表中的数据再转换为JSON字符串
    url(r"^json-users-09/$",views.jsonusers_views),
    # １０
    url(r"^json-display-08A",views.json_displayA),
    url(r'^json-display-08B/$',views.json_displayB),
    # １１　前端中将JS对象转换为JSON字符串
    url(r"^front-json-11/$",views.front_viewsA),
    url(r"^server-json-11/$",views.front_viewsB),
    # １２ 前后端交互转换
    url(r"^user-login-A/$",views.user_loginA),
    url(r"user-login-B/",views.user_loginB),
    # １３　演示jquery中的$obj.load()方法的使用
    url(r"^head-13/$",views.head_views),
    url(r"^^index-13/$",views.index_views),
    # １４　演示jquery中的$.get()方法的使用
    url(r"^jquery-get-14/$",views.jquery_views),
    # １５　通过$.get()完成搜索建议
    url(r"^search-15/$",views.search_views),
    url(r"^server-15/$",views.server15_views),
    # 16 通过$.ajax完成自定义的ajax请求
    url(r"^ajax-jq-16/$",views.jqajax_views),
]
