"""
file : user/views.py
"""
import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from tokens.views import make_token
from users.models import UserIntro


def register_view(request,username=None):
    """
    用户注册
    :param request:
    :return:
    """
    if request.method != "POST":
        response_content = {"code": 404, "error": " The request method is Error !!!"}
        return JsonResponse(response_content)

    if request.method == "POST":
        # 接受客户端请求：json串
        json_str = request.body
        if not json_str:
            # 请求为空情况下
            response_content = {"code": 202, "error": " The request content is empty !!!"}
            return JsonResponse(response_content)
        # 　json格式请求需要转换
        request_str = json.loads(json_str)
        # 提取信息
        username = request_str.get("username")
        email = request_str.get("email")
        password1 = request_str.get("password_1")
        password2 = request_str.get("password_2")
        if not username:
            response_content = {"code": 203, "error": "The username is empty !!!"}
            return JsonResponse(response_content)
        if not email:
            response_content = {"code": 204, "error": "The email is empty !!!"}
            return JsonResponse(response_content)
        if not password1 or not password2:
            print(password2, password1)
            response_content = {"code": 205, "error": "The password is empty !!!"}
            return JsonResponse(response_content)
        if password1 != password2:
            response_content = {"code": 206, "error": "Two different passwords !!!"}
            return JsonResponse(response_content)
        # 判断用户是否存在
        exist_user = UserIntro.objects.filter(username=username)
        if exist_user:
            response_content = {"code": 207, "error": "The username is exist !!!"}
            return JsonResponse(response_content)
        # 密码散列运算
        hs = hashlib.sha256()  # sha创建对象
        hs.update(password2.encode())  # 添加要hashlib的字节串内容
        # 创建用户
        try:
            UserIntro.objects.create(username=username,
                                     email=email,
                                     password=hs.hexdigest())  # 存储16进制散列算法结果密码
        except Exception as e:
            response_content = {"code": 500, "error": "Exception is  %s !!!" % (e)}
            return JsonResponse(response_content)

        # 生成token，调用make_token方法，返回结果为字节串
        token = make_token(username)
        # 发送token  注意事项：token接收值为bytes字节串不能json,字节串先转换为字符串再转换json串发送
        response_content = {"code": 200,
                            "username": username,
                            "data": {"token": token.decode()}}  # 此次会话用令牌token
        return JsonResponse(response_content)


def username_view(request, username=None):
    """
    获取指定用户数据
    http://127.0.0.1:5000/hfklswn/info
    :param request:
    :param username:用户名
    :return:
    """
    if request.method != "GET":
        response_content = {"code": 404, "error": " The request method is Error !!!"}
        return JsonResponse(response_content)

    if request.method == "GET":
        # 如果用户名不存在获取所有用户数据
        if username:
            usernames = UserIntro.objects.filter(username=username)
            if not usernames:
                response_content = {"code": 208, "error": " The username is Error !!!"}
                return JsonResponse(response_content)
            a_username = usernames[0]
            GET_keys = request.GET.keys()  # 获取get请求方式的所有数据的QueryDict查询字典的对象的所有键
            print(GET_keys)
            if GET_keys:
                data = {}
                for key in GET_keys:
                    if key == "password":
                        continue  # 如果用户获取密码跳过本次获取请求
                    # hasattr()函数和getattr()函数搭配使用
                    if hasattr(a_username, key):
                        if key == "avatar":
                            print(key)
                            # 属性avatar需要调用str方法 __str__
                            data[key] = str(getattr(a_username, key))
                        else:
                            data[key] = getattr(a_username, key)
                        print(data)
                response_content = {"code": 200, "username": username, "data": data}
                return JsonResponse(response_content)
        # 如果用户名存在获取指定用户数据
            else:
                response_content = {"code": 200, "username": username, "data": {
                    "nickname": a_username.nickname,
                    "email": a_username.email,
                    "sign": a_username.sign,
                    "info": a_username.info,
                    "avatar": str(a_username.avatar)}}
                return JsonResponse(response_content)
