import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# fele:afax/views.py


# createxhr_01.html


def create_views(request):
    return render(request, "createxhr_01.html", locals())


def server02_views(request):
    return HttpResponse("这是server02的响应")


def ajaxget_views(request):
    return render(request, "ajax-get-02.html")


def getparams_views(request):
    return render(request, "ajax-grt-params-03.html")


def server03_views(request):
    # 1 接受前段传递过来的两个参数
    name = request.GET["name"]
    age = request.GET["age"]
    # 2 响应数据给前段
    s = "姓名：%s 年龄：%s" % (name, age)
    return HttpResponse(s)


def register_views(request):
    return render(request, "register-04.html", locals())


from .models import Users


def checkunme_views(request):
    # 1.接收前端传递过来的 - uname
    uname = request.GET.get("uname", "Not Name")
    # 2.判断uname在User实体中是否存在[查询操作]
    users = Users.objects.filter(uname=uname)
    # 3. 根据查询结果给出响应
    if users:
        return HttpResponse("1")
    return HttpResponse("创建成功")


def reguser_views(request):
    # １接收前端传递的数据
    uname = request.GET.get("uname", "Not Name")
    upwd = request.GET.get("upwd", "Not Password")
    uemail = request.GET.get("uemail", "Not Email")
    nickname = request.GET.get("nickname", "Not Nickname")
    # ２通过实体类实现增加功能(通过异常处理解决增加失败的问题)
    try:
        Users.objects.create(uname=uname, upwd=upwd, uemail=uemail, nickname=nickname)
        return HttpResponse("1")
    except Exception as ex:
        print(ex)
        return HttpResponse("0")


def regpost_views(request):
    # １接收前端传递的数据
    print(request)
    uname = request.POST.get("uname", "Not Name")
    upwd = request.POST.get("upwd", "Not Password")
    uemail = request.POST.get("uemail", "Not Email")
    nickname = request.POST.get("nickname", "Not Nickname")
    # ２通过实体类实现增加功能(通过异常处理解决增加失败的问题)
    try:
        Users.objects.create(uname=uname, upwd=upwd, uemail=uemail, nickname=nickname)
        return HttpResponse("1")
    except Exception as ex:
        print(ex)
        return HttpResponse("0")


def post_views(request):
    return render(request, "post-05.html", locals())


def server05_views(request):
    uname = request.POST["uname"]
    upwd = request.POST["upwd"]
    msg = "用户名：%s 密码：%s" % (uname, upwd)
    return HttpResponse(msg)


def users_views(request):
    return render(request, "display_user-06.html", locals())


def server06_views(request):
    msg = ""
    users = Users.objects.all()
    for s in users:
        msg += "%s&%s&%s&%s&%s|" % (s.id, s.uname, s.upwd, s.uemail, s.nickname)
    msg = msg[0:-1]  # 去掉|
    return HttpResponse(msg)


def json_views(request):
    return render(request, "json-07.html", locals())


def jsonserver_views(request):
    # 1. 使用字典来表示JSON数据
    dic = {
        "course": "Ajax", "duration": 3, "place": "BJ",
    }
    # 将dic通过Json.dumps转换为JSON格式的字符串,返回值为json字符串
    jsonStr = json.dumps(dic)  # 只能传递给dumps一个参数
    # 使用列表表示多个JSON数据(列表封装字典)
    lis = [dic, {"a": 1, "b": 2, "c": "pig"}, ]
    return HttpResponse(lis)


def jsonusers_views(request):
    users = Users.objects.all()
    # user =json.dumps(users)
    # return HttpResponse(user)
    jsonUser = serializers.serialize("json", users)
    return HttpResponse(jsonUser)

def json_displayA(request):
    return render(request, "json_display-08.html", locals())

def json_displayB(request):
    users = Users.objects.all()
    jsonUser = serializers.serialize("json", users)
    return HttpResponse(jsonUser)

def front_viewsA(request):
    return render(request, "front-json-11.html", locals())


def front_viewsB(request):
    jsonStr = '{"uname": "wang","uage": 30,"ugender": "unknown"}'
    # 通过json.loads()--服务器端将JSON字符串转换为字典/列表
    dic = json.loads(jsonStr)
    s = "姓名：%s,年龄：%d,性别：%s"%(dic["uname"],dic["uage"],dic["ugender"])
    return HttpResponse(s)

def user_loginA(request):
    return render(request,"user_login.html",locals())

def user_loginB(request):
    params = request.GET["params"]
    # 将params转换成Python字典
    dic = json.loads(params)
    try:
        Users.objects.create(uname=dic["username"],upwd=dic["userpassword"],uemail=dic["useremail"],nickname=dic["usernickname"])
        return HttpResponse("注册成功")
    except:
        return HttpResponse("注册失败")

def head_views(request):
    return render(request,"head-13.html",locals())

def index_views(request):
    return render(request,"index-13.html",locals())


def jquery_views(request):
    return render(request,"jquery-get-14.html",locals())


def search_views(request):
    return render(request,"search-15.html",locals())

def server15_views(request):
    # １．接收前端传过来的参数
    kw = request.GET.get("kw","w")
    # 2.查询User实体中uname列中包含前端传来数据的信息
    users = Users.objects.filter(uname__contains=kw)
    # 3. 将uname封装成列表再转换成JSON串响应
    ulist = []
    if users:
        for u in users:
            ulist.append(u.uname)
    return HttpResponse(json.dumps(ulist))

def jqajax_views(request):
    return render(request,"jq-ajax-16.html",locals())

