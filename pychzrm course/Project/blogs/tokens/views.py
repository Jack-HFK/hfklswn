import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from users.models import UserIntro


def tokens_view(request):
    """
    创建token ---> 登录
    :param request:
    :return:
    """
    # http://127.0.0.1:8000/v1/tokens
    if not request.method == "POST":
        response_content = {"code": 201, "error": "The response is not POST  !!!"}
        return JsonResponse(response_content)
    # 接受客户端请求：json串
    json_str = request.body
    if not json_str:
        # 请求为空情况下
        response_content = {"code": 202, "error": " The request content is empty !!!"}
        return JsonResponse(response_content)
    # 　json格式请求需要转换
    request_str = json.loads(json_str)
    username = request_str.get("username")
    password = request_str.get("password")
    if not username:
        response_content = {"code": 203, "error": " The  username is empty !!!"}
        return JsonResponse(response_content)
    if not password:
        response_content = {"code": 205, "error": " The  password is empty !!!"}
        return JsonResponse(response_content)
    # 查找用户是否存在
    a_username = UserIntro.objects.filter(username=username)
    if not a_username:
        response_content = {"code": 208, "error": " The  username does not exist !!!"}
        return JsonResponse(response_content)

    # 密 码 验 证
    # 密码散列运算
    hs = hashlib.sha256()  # sha创建对象
    hs.update(password.encode())  # 添加要hashlib的字节串内容
    # 判断密码SHA-256后的16进制是否与数据库存储的密码一致
    if hs.hexdigest() != a_username[0].password:
        response_content = {"code": 209, "error": " The password is Error !!!"}
        return JsonResponse(response_content)


# 生成token发送给前端浏览器
# 生成token，make_token方法返回结果为字节串
    token = make_token(username)
    # 发送token  注意事项：token接收值为bytes字节串不能json,字节串先转换为字符串再转换json串发送
    response_content = {"code": 200,
                        "username": username ,
                        "data":{"token":token.decode()}}  # 此次会话用令牌token
    return JsonResponse(response_content)


def make_token(username, expire=3600 * 24):
    """
    生成token,客户端校验用户使用
    :param username: 用户
    :param expire: 用户存在时间
    :return:
    """
    key = "hfk"  # 密钥
    present_time = time.time()  # 当前时间时间
    statement = {"username": username, "exp": int(present_time + expire)}
    # 注意：返回类型为字节串
    return jwt.encode(statement, key, algorithm="HS256")