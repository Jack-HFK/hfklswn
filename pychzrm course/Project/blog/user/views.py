import hashlib
import json
import time
import jwt
# from blog.btoken.views import make_token_view

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

# from Project.code.blog.user.models import UserProfile


# Create your views here.

# file : user/views.py
from btoken.views import make_token_view
from .models import UserProfile
from tools.login_check import login_check


# @check_token("PUT", "POST", "GET")  # 参数为告诉装饰器那些方法需要进行check_token方法校验
@login_check("PUT")
def users_view(request, username=None):
    if request.method == "POST":
        # 注册
        # 接收用户json数据，字节串需转换为字符串
        json_str = request.body.decode()
        if not json_str:
            result = {"code": 202, "error": "Please POST"}
            return JsonResponse(result)
        # 如果当前报错，请执行json_str = json_str.decode()
        # 服务器端将JSON字符串转换为字典/列表格式字符串loads()
        json_str = json.loads(json_str)
        username = json_str.get("username")
        email = json_str.get("email")
        password_1 = json_str.get("password_1")
        password_2 = json_str.get("password_2")
        # JsonResponse("传入的数据") 传入的数据直接转换为json串，省略的服务端json串的转换
        if not username:
            result = {"code": 203, "error": "Please give me your name"}
            return JsonResponse(result)
        if not email:
            result = {"code": 204, "error": "Please give me email"}
            return JsonResponse(result)
        if not password_1 or not password_2:
            result = {"code": 205, "error": "Please give me password !"}
            return JsonResponse(result)
        if password_1 != password_2:
            result = {"code": 206, "error": "用户名已经存在"}
            return JsonResponse(result)

        # 检查用户名是否存在
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {"code": 207, "error": "用户名已经存在"}
            return JsonResponse(result)
        # 密码散列
        p_m = hashlib.sha256()  # 创建256对象
        p_m.update(password_1.encode())  # 转换字节串，接受json串，把json串转换,ha256加密

        try:
            UserProfile.objects.create(username=username,
                                       nickname=username,
                                       email=email,
                                       password=p_m.hexdigest())
        except Exception as e:
            result = {"code": 500, "error": "Sorry,server is busy !"}
            return JsonResponse(result)

        token = make_token_view(username)
        result = {"code": 200, "username": username, "data": {"token": token.decode()}}
        return JsonResponse(result)

    elif request.method == "GET":
        # 获取数据
        if username:
            # 　获取指定用户数据
            users = UserProfile.objects.filter(username=username)
            if not users:
                result = {"code": 208, "error": "The username is not existed !"}
                return JsonResponse(result)
            user = users[0]
            if request.GET.keys():  # 获取键
                # 当前请求有查询字符串
                data = {}
                for key in request.GET.keys():
                    if key == "password":
                        # 如果查询密码，则跳过
                        continue
                    # hasattr 第一个参数：对象 ，第二个参数：属性值字符串 ，返回值True/False
                    # 若对象含有第二个参数的属性，则返回True 反之False
                    # getattr 第一个参数：对象 ，第二个参数：属性值字符串
                    # 若对象含有第二个参数的属性，则返回对应的属性值，反之抛出异常 AttributeError
                    if hasattr(user, key):
                        if key == "avatar":  # 默认没有头像时传递的为avatar的默认头像
                            # 属性avatar需要调用str方法 __str__
                            data[key] = str(getattr(user, key))
                        else:
                            data[key] = getattr(user, key)
                        # data[key] = getattr(user, key)
                    result = {"code": 200, "username": username, "data": data}
                return JsonResponse(result)
            else:
                # 如果没有查询字符串
                result = {"code": 200, "username": username,
                          "data": {"info": user.info,
                                   "sign": user.sign,
                                   "nickname": user.nickname,
                                   "avatar": str(user.avatar)}}

            return JsonResponse(result)
        else:
            # 没有username
            users_all = UserProfile.objects.all()
            result = []
            for _user in users_all:
                d = {}
                d["username"] = _user.username
                d["nickname"] = _user.nickname
                d["sigon"] = _user.sign
                d["info"] = _user.info
                d["email"] = _user.email
                d["avatar"] = str(_user.avatar)
                result.append(d)
            return JsonResponse({"code": 200, "data": result})

        # 获取指定的用户数据
    elif request.method == "PUT":
        # 前端访问地址为 http://127.0.0.1:5000/<username>/change_info
        # 后段地址为http://127.0.0.1:8000/v1/users/<username>
        # 　更新用户数据
        # user = check_token(request)
        user = request.user
        # if not user:
        #     result = {"code": 209, "error": "The PUT need token"}
        #     return JsonResponse(result)
        json_str = request.body.decode()
        json_obj = json.loads(json_str)
        nickname = json_obj.get("nickname")
        if not nickname:
            result = {"code": 210, "error": "The nickname is can not be none !"}
            return JsonResponse(result)
        sign = json_obj.get("sign")
        if sign is None:
            result = {"code": 211, "error": "The sign not in json !!!"}
            return JsonResponse(result)
        info = json_obj.get("info")
        if info is None:
            result = {"code": 212, "error": "The info nt in json !!!"}
            return JsonResponse(result)
        if user.username != username:
            result = {"code": 213, "error": "This is wrong !!!"}
            return JsonResponse(result)
        user.sign = sign
        user.info = info
        user.nickname = nickname
        user.save()
        result = {"code": 200, "username": username}
        return JsonResponse(result)


def check_token(request):
    # 获取authorization
    token = request.META.get("HTTP_AUTHORIZATION")
    if not token:
        return None
    try:
        res = jwt.decode(token, "hfk")
    except Exception as e:
        print("check_token error is %s" % (e))
        return None
    username = res["username"]
    users = UserProfile.objects.filter(username=username)  # filter返回列表
    return users[0]

@login_check("POST")
def user_avatar_view(request,username):
    """
    更换图片
    只开放POST请求
    :param request:
    :return:
    """

    if request.method != "POST":
        result ={"code":214,"error":"Please use"}
        return JsonResponse(result)
    # 获取用户
    user = request.user
    if user.username != username:
        # 异常请求
        result = {"code":215,"error":"You are wrong !!!"}
        return JsonResponse(result)
    # 获取上传图片，长传方式是表单
    avatar = request.FILES.get("avatar")
    if not avatar:
        result = {"code":216,"error":"Please give me avatar !!"}
        return JsonResponse(result)
    # 更新保存图片
    user.avatar = avatar
    user.save()
    result = {"code":200,"username":username}
    return JsonResponse(result)









