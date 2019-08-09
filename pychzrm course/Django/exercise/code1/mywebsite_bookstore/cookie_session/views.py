from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden


# Create your views here.

# 添加或修改cookie
def set_cookie_view(request):
    # 方法一：
    # 生成HttpResponse对象
    hr_object = HttpResponse("hr是HttpResponse对象")
    # 利用 set_cookie 创建cookie
    hr_object.set_cookie("key", "price")
    return hr_object


# def set_cookie_view(request):
#     # 方法二：
#     # 生成HttpResponse对象
#     hr_object = render(request, "cookie_session.html", locals())  # hr是HttpResponse对象
#     # 利用 set_cookie 创建cookie
#     hr_object.set_cookie("key", "price")  # set_cookie("字典键","字典值")
#     return hr_object

# def set_cookie_view(request):
#     # 方法三：
#     from django.shortcuts import redirect
#     hr_object = redirect('/')  # redirect('/')  路由重定向到http://127.0.0.1:8000/
#     hr_object.set_cookie('key', "price")  # set_cookie('cookies名', cookies值, 超期时间)
#     return hr_object

# 获取cookie
def get_cookie_view(request):
    # 获得到具体一个cookie
    a_cookie = request.COOKIES["a_cookie"]  # cookie是键值对的方式存储
    dict_object = request.COOKIES  # 接收字典
    s = str(dict_object)  # 转为字符串
    return HttpResponse(s,a_cookie)
