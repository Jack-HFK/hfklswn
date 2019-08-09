from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# file : user/views.py

from . import models

def login_view(request):

    # if 'user' in request.session:
    #     print("用户已登陆")
    # else:
    #     print("用户没登陆")

    # 尝试操作session
    # value = request.session.get('mypassword', '没有设置密码')
    # print("密码是:", value)

    if request.method == "GET":
        username = request.COOKIES.get('myname', '')
        return render(request, 'user/login.html',
                      locals())
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        # 表单验证(验证用户提交的数据是否合法)
        if username == '':
            name_error = '请填写用户名!!!'
            return render(request, 'user/login.html',
                          locals())
        password = request.POST.get('password', '')
        # 用session 来保存密码
        # request.session['mypassword'] = password

        remember = request.POST.get('remember', '')

        # 进行登陆逻辑的操作
        try:
            auser = models.User.objects.get(
                username=username, password=password
            )
        except:
            password_error = "用户名或密码不正确！！"
            return render(request, 'user/login.html',
                          locals())
        # 如果能走到此外．说明用户名密码正确，
        # 在session里标记用户是登陆状态
        request.session['user'] = {
            'name': auser.username,
            'id': auser.id
        }

        resp = HttpResponse('提交成功: remember='+remember)
        if remember == '1':
            resp.set_cookie('myname', username, max_age=7*24*60*60)
        else:
            resp.delete_cookie('myname')
        return resp

def logout_view(request):
    # 退出登陆
    if 'user' in request.session:
        del request.session['user']
    # 返回到主页
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/')





