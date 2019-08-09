from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from . import models

# file :user/views.py

def login_view(request):
    if "user" in request.session:
        print("用户已经登录")
    else:
        print("用户没有登录")
    if request.method == "GET":
        username = request.COOKIES.get("myname","")
        return render(request,"user/login.html",locals())
    elif request.method == "POST":
        username = request.POST.get("username","")
        # 表单验证（验证用户输入的数据是否合法）
        if username == "":
            name_error = "请填写用户名"
            return render(request,"user/login.html",locals())
        password = request.POST.get("password","")
        remember = request.POST.get("remember","")

        # 进行登录逻辑操作
        try:
            auser = models.User.objects.get(username=username, password = password)
        except:
            password_error = "用户名密码不正确"
            return render(request,"user/login.html",locals())

        # 如果能走到此处，说明用户名密码正确，在session中标识当前用户是登陆状态
        request.session["user"] = {
            "name" : auser.username,
            "id" : auser.id
        }

        # resp = HttpResponse("提交成功!  remember = " + remember)
        resp = HttpResponseRedirect("/")

        if remember == "1":
            resp.set_cookie("myname",username,)
        else:
            resp.delete_cookie("myname")
        return resp

def logout_view(request):
    # 退出登录
    if "user" in request.session:
        del request.session["user"]
    # 退出后返回主页
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect("/") # 重定向到主页