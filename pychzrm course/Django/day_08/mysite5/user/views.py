from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from . import models

# file :user/views.py

# 登录
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

def reg_view(request):
    if request.method == "GET":
        return render(request,"user/reg.html",locals())
    elif request.method == "POST":
        user_name = request.POST.get("user_name","")
        try:
            models.User.objects.get(username=user_name)
            name_error = "用户名已存在"
            return render(request,"user/reg.html",locals())
        except:
            password1 = request.POST.get("user_password","")
            password2 = request.POST.get("user_password2","")
            if not password1 or not password2:
                no_password = "密码不能为空"
                return render(request,"user/reg.html", locals())
            if password1 != password2:
                no_password = "输入的密码不相同"
                return render(request,"user/reg.html",locals())
            new_name = models.User.objects.create(username=user_name,password=password1)
            happy = "欢迎登陆吃鸡战场 <a href='/'>进入战场</a> "
            return HttpResponse(happy)






# 退出
def logout_view(request):
    # 退出登录
    if "user" in request.session:
        del request.session["user"]
    # 退出后返回主页
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect("/") # 重定向到主页





from . import forms

def reg2_view(request):
    if request.method == "GET":
        reg2 = forms.Reg2()   # reg2对象是表单控件
        return render(request,"user/reg2.html",locals())
    elif request.method == "POST":
        # 如何拿到表单数据
        # 方法一：request.POST
        # 方法二:
        form = forms.Reg2(request.POST)
        if form.is_valid():   #is_valid() 表单验证
            html = str(form.cleaned_data)  # 　cleaned_data干净的数据
            return HttpResponse(html)
        else:
            return HttpResponse("提交的数据不合法")

