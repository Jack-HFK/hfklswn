from django.shortcuts import render

# Create your views here.
# file : note/views.py

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models
from user.models import User

# 写一个函数装饰器,检查用户是否登陆,如果没有登陆,
# 则直接跳转到登陆页面
def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        else:
            return fn(request, *args, **kwargs)
    return wrap


def add_view(request):
    # 检查用户是否登陆,如果没有登陆,进入登陆页面
    if 'user' not in request.session:
        return HttpResponseRedirect('/user/login')

    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        # 根据登陆用户的id 找到此用户
        try:
            a_user = User.objects.get(
                id=request.session['user']['id'])
        except:
            return HttpResponse("登陆用户数据错误")
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        # 根据表单内容来创建记录
        models.Note.objects.create(
            title=title,
            content=content,
            user = a_user
        )
        return HttpResponseRedirect('/note/')


from django.core.paginator import Paginator
@check_login
def list_view(request):
    # 检查用户是否已经登陆,如果没有登陆

    try:
        a_user_id = request.session['user']['id']
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    notes = a_user.note_set.all()  # 获取当前用户所有笔记
    # return render(request, 'note/list_note.html',
    #               locals())

    # 把 notes 以每页5条数据进行分页
    paginator = Paginator(notes, 5)
    print("分页前的数据个数", paginator.count)
    print("当前页面的个数是:", paginator.num_pages)
    print("page_range=", paginator.page_range)

    # 先得到当前的页码信息,如果没有?page=xxx, 返回第1页信息
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)

    return render(request, 'note/list_note2.html',
                  locals())

@check_login
def del_view(request, id):
    # 先得到当前用户信息
    try:
        a_user_id = request.session['user']['id']
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    # 再根据用户和 id 找到对应的笔记
    a_note = a_user.note_set.get(id=id)
    a_note.delete()  # 删除
    return HttpResponseRedirect('/note/')



@check_login
def mod_view(request, id):
    # 先得到当前用户信息
    try:
        a_user_id = request.session['user']['id']
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    # 再根据用户和 id 找到对应的笔记
    a_note = a_user.note_set.get(id=id)

    if request.method == 'GET':
        return render(request, 'note/mod_note.html',
                      locals())
    elif request.method == 'POST':
        # 从表单提取数据
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        # 修改对应的数据
        a_note.title = title
        a_note.content = content
        a_note.save()
        return HttpResponseRedirect('/note/')




