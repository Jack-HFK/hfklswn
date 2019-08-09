from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from user.models import User

# 装饰器函数，检查用户是否登录。没有登录直接跳转到登录页面
def check_login(fn):
    def wrap(request,*args,**kwargs):
        # 检查用户是否登录，没有登录返回登录页面，不让进入编辑页面
        if "user" not in request.session:
            return HttpResponseRedirect("/user/login")
        else:
            return fn(request,*args,**kwargs)
    return wrap
# Create your views here.

def add_view(request):
    # 检查用户是否登录，没有登录返回登录页面，不让进入编辑页面
    if "user" not in request.session:
        return HttpResponseRedirect("/user/login")
    if request.method == "GET":
        return render(request, "note/add_note.html", locals())
    elif request.method == "POST":
        # 根据登录用户的id找到此用户
        try:
            a_user = User.objects.get(
                id=request.session["user"]["id"])
        except:
            return HttpResponse("登录用户数据错误")
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        models.Note.objects.create(
            title=title,
            content=content,
            user=a_user
        )
        return HttpResponseRedirect("/note/")

from django.core.paginator import Paginator
@check_login
def list_view(request):
    # 检查用户是否已经登录
    try:
        a_user_id = request.session["user"]["id"]
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    notes = a_user.note_set.all() # 获取当前用户所有笔记
    # return render(request,"note/list_note.html",locals())

    # 把　notes 以每页５条的数据进行分页
    paginator = Paginator(notes,5)

    # 先得到当前的页码信息，如果没有?page= xxx,返回第一页信息
    page_number = request.GET.get("page",1)
    page = paginator.page(page_number)

    return render(request,"note/list_note2.html",locals())

@check_login
def del_view(request, id):
    # 先得到当前用户信息
    try:
        a_user_id = request.session["user"]["id"]
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    # 再根据用户和id找到对应的笔记
    a_note = a_user.note_set.get(id = id)
    a_note.delete()
    return HttpResponseRedirect("/note/")





@check_login
def mod_view(request, id):
    # 先得到当前用户信息
    try:
        a_user_id = request.session["user"]["id"]
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    # 根据id获取跟人全部信息
    a_note = a_user.note_set.get(id=id)
    if request.method == "GET":
        return render(request,"note/mod_note.html",locals())
    elif request.method == "POST":
        # 从表单接受数据
        title = request.POST.get("title","")
        content = request.POST.get("content","")
        # 修改用户信息
        a_note.title = title
        a_note.content = content
        # 改完保存下
        a_note.save()
        return HttpResponseRedirect("/note/")