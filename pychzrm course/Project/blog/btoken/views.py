import hashlib
import json
import time

import jwt
from django.http import JsonResponse




# file : btoken/views.py
# Create your views here.
from user.models import UserProfile


def tokens_view(request):
    """
    创建token --> 登录请求
    :param request:
    :return:
    """
    if not request.method == "POST":
        result = {"code": 102, "error": "Please use POST !!"}
        return JsonResponse(result)
    json_str = request.body  # 接收用户json数据
    if not json_str:
        result = {"code": 103, "error": "Please give me json"}
        return JsonResponse(result)
    json_obj = json.loads(json_str.decode())
    username = json_obj.get("username")
    password = json_obj.get("password")
    if not username:
        result = {"code": 104, "error": "Please give me username"}
        return JsonResponse(result)
    if not password:
        result = {"code": 105, "error": "Please give me password"}
        return JsonResponse(result)
    ausername = UserProfile.objects.filter(username=username)
    if not ausername:
        result = {"code": 106, "error": "Your username or password is wrong !"}
        return JsonResponse(result)
    # 生成密码hash
    apassword = hashlib.sha256()
    apassword.update(password.encode())
    if ausername[0].password != apassword.hexdigest():
        result = {"code":107,"error":"The username or password is wrong !"}
        return JsonResponse(result)

    # 生成token
    token = make_token_view(username)
    result = {"code":200,"username":username,"data":{"token":token.decode()}}
    return JsonResponse(result)





def make_token_view(username, expire=3600 * 24):
    """
    生成token()
    :param username:
    :param expire:
    :return:
    """
    key = "hfk"
    now_t = time.time()
    data = {"username": username, "exp": int(now_t + expire)}
    return jwt.encode(data, key, algorithm="HS256") # 返回值token串

