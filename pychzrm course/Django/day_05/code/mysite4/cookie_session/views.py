from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def set_cookies(request):
    resp = HttpResponse("OK")
    resp.set_cookie('cookies名', "cookies值")# 超期时间
    return resp

def get_cookie(request):
    # 得到浏览器aaa对应的值
    v = request.COOKIES["aaa"]
    print("v=",v)

    dic = request.COOKIES # dic接收返回字典
    s = str(dic) # 把字典转为字符串
    return HttpResponse(s)