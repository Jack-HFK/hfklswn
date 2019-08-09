from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# /cs/set_cookie
def set_cookie(request):
    # 方法１
    # resp = HttpResponse("OK")
    # resp.set_cookie('aaa', 'bbb')
    # return resp
    # 方法２
    # 方法3
    from django.shortcuts import redirect
    resp = redirect('/bookstore/books')
    resp.set_cookie('myname', 'weimz')
    return resp

# /cs/get_cookie
def get_cookie(request):
    # 得到浏览器端 aaa 对应的值
    v = request.COOKIES['aaa']
    print('v=', v)

    dic = request.COOKIES
    s = str(dic)  # 把字内转为字符串
    return HttpResponse(s)







