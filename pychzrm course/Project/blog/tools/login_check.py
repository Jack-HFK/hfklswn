"""
检验 token
"""
import jwt
from django.http import JsonResponse

from user.models import UserProfile

TOKEN_KEY = "hfk"


def login_check(*methods):
    """
    获取token
    :param methods: 请求（GET/POST/....
    :return:
    """
    def _login_check(func):
        def wrapper(request, *args, **kwargs):
            # 获取token
            token = request.META.get("HTTP_AUTHORIZATION")
            if not methods:
                # 如果当前没有传入任何参数，则直接返回视图函数
                return func(request, *args, **kwargs)
            else:
                # 　检查当前request.method 是否在参数列表中
                if request.method not in methods:
                    return func(request, *args, **kwargs)
            if not token:
                result = {"code": 109, "error": "Please give me token !!"}
                return JsonResponse(result)

            # 校验token是否正确
            try:
                res = jwt.decode(token, TOKEN_KEY)
                # print(res) # {'username': 'hfk', 'exp': 1564623088}
            except Exception as e:
                print("login check is error %s" % (e))
                result = {"code": 108, "error": "The token is wrong !!"}
                return JsonResponse(result)
            # token校验成功
            username = res["username"]
            try:
                user = UserProfile.objects.get(username=username)
            except:
                user = None
            if not user :
                result = {"code":110,"error":"The user is not existed !!"}
                return JsonResponse(result)

            # 将user　赋值　user对象
            request.user = user

            return func(request, *args, **kwargs)

        return wrapper

    return _login_check


def get_user_by_request(request):
    """
    通过request 获取 user
    :param request:
    :return:
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    if not token:
        return None
    # 尝试解析token
    try:
        res = jwt.decode(token,TOKEN_KEY)
    except:
        return None
    # 解析成功　提取用户名
    username = res["username"]
    # 提取数据库用户名,判断用户是否存在
    user = UserProfile.objects.get(username=username)
    if not user:
        return None
    return user



