# file :mywebsite_bookstore/views
from django.http import HttpResponse  # 调用响应处理模块
from django.template import loader
from django.shortcuts import render


def number_view(request,str,number):
    if request.method == "GET":
        # a = request.GET["a"] # 获取客户端请求 GET 请求提交的数据
        # b = request.GET.get("b","默认值")
        c = request.GET.getlist("c")
        # HttpResponse把处理结果响应给客户端浏览器
        # return HttpResponse("以关键字传参方式传入" + b )
        return HttpResponse(c)
    elif request.method == "POST":
        # request.path_info :URL 字符串
        return HttpResponse(request.path_info)

#  通过 loader 获取模板 , 通过 HttpResponse 进行响应
def templates1_view(request):
    # 通过loder加载模板
    t = loader.get_template("templates1.html")
    # 将ｔ装换为HTML字符串
    html = t.render({"变量1":88})
    # 用响应对象将转换的字符串内容返回给浏览器
    return HttpResponse(html)
# 模板传参是指把数据形成字典,传参给模板,为模板渲染提供数据
#   使用 render() 直接加载并响应模板
def templates2_view(request):
    return render(request,"templates2.html",{"变量2":"值2"})

def templates3_view(request):
    name3 = "值３"
    name4 = 15
    print(locals())
    # locals()直接将局部变量组合成字典形式{变量名:值,变量名:值 ... ...}
    return render(request,"temlplates3.html",locals())


def urlfan_view(request,m):
    urlfan = "反向解析"
    return render(request,"urlfan.html",locals())









