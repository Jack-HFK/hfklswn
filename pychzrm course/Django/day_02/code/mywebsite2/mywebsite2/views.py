from django.http import HttpResponse


def sum_view(request):
    if request.method == "GET":
        start = request.GET.get("start","0")
        stop = request.GET["stop"]
        step = request.GET.get("start","1")
        start,stop,step = int(start),int(stop),int(step)
        result = sum(range(start,stop,step))
    return HttpResponse("结果是：" + str(result))

html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/test_post" method="post">
        <input type="text" name="search_name" >
        <input type="submit" value="开始搜索" >
    </form>
</body>
</html>
"""

def test_pst_view(request):
    if request.method == "GET":
        return HttpResponse(html)
    elif request.method == "POST":
        # input标签提交的name为字典键
        value = request.POST["search_name"]
        return HttpResponse("search_name = " + value)

# 方法一
from django.template import loader
def test1_view(request):
        # t绑定模板对象(路径)
        t = loader.get_template("myhomepage.html")
        # 用模板生成html
        html = t.render()
        # 返回浏览器
        return HttpResponse(html)

# 方法二
from django.shortcuts import render
def test1_view(request):
    return render(request,"myhomepage.html")

def test2_view(request):
    person = {
        "name" : "动态调整",
        "age" : "25"
    }
    # 模板传参是指把数据形成字典,传参给模板,为模板渲染提供数据
    # 在模板中使用变量语法
    # {{变量名}}
    # 视图函数中必须将变量封装到字典中才允许传递到模板上
    return render(request,"myhomepage.html",person)

# <!--通过变量调用视图中的数据-->
#  视图中更改数据模板中省略了改动（低耦合）
def mypage2_view(request):
    myvar = 999
    mystr = "hellow"
    mylist = ["上海","日本"]
    preson = {"name":"tedu","age":10}
    money = 9999
    def myfun():
        return "函数结果"
    # 类名.函数名 = 数据
    city = ["日本", "美国","英国","澳大利亚"]

    return render(request,"mypage2.html",locals())

def page0_view(request):
    return render(request,"mybase.html")
def page1_view(request):
    return render(request,"page1.html")
def page2_view(request):
    return render(request,"page2.html")


# 以下用page3 和 page/(\d+) 表示url反向解析

def page3_view(request):
    return render(request,"page3.html")

def pagen_view(request,n):
    return render(request,"pagen.html",locals())