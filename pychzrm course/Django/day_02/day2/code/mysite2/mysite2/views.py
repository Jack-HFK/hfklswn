
# file : mysite2/views.py


from django.http import HttpResponse


def sum_view(request):
    if request.method == 'GET':
        start = request.GET.get('start', '0')
        stop = request.GET['stop']
        step = request.GET.get('step', '1')
        start, stop, step = int(start),int(stop), int(step)
        result = sum(range(start, stop, step))

    return HttpResponse("结果: %d" % result)

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="/test_post" method="post">
        <input type="text" name="search_name">
        <select name="gender">
            <option value=1>男</option>
            <option value=0>女</option>
        </select>
        <textarea name="comment" rows="5" cols="10">附言...</textarea>

        <input type="submit" value="开始搜索">
    </form>
</body>
</html>
'''

def test_post_view(request):
    if request.method == 'GET':
        return HttpResponse(html)
    if request.method == 'POST':
        value = request.POST['search_name']
        dic = dict(request.POST)
        return HttpResponse("search_name=" + value + str(dic))


from django.template import loader

from django.shortcuts import render
def test1_view(request):

    person = {
        # 'name': 'tedu',
        # 'age': 19
        'name': '魏明择',
        'age': 35
    }

    # 方法2
    return render(request, 'myhomepage.html', person)

    # 方法1
    # # t绑定模板对象
    # t = loader.get_template("myhomepage.html")
    # # 用模板生成html
    # html = t.render()
    # # 返回给浏览器
    # return HttpResponse(html)

class Dog:
    def show_info(self):
        return "小黄狗"

def mypage2_view(request):
    myvar = 999
    mystr = "hello world!"
    mylist = ["北京",'上海', '深圳']
    person = {"name": "tedu", 'age':18}
    dog1 = Dog()

    def myfun1():
        return "函数结果！！！"
    # myfun = lambda : "函数结果！！！"

    money = 999999999  # 大于1亿富翁，大于1亿富翁10万有钱

    city = ["北京",'上海', '深圳', '重庆']
    # city = []

    return render(request, 'mypage2.html', locals())

    # return render(request, 'mypage2.html',
    #               {'myvar': myvar})


def page0_view(request):
    return render(request, 'mybase.html')


def page1_view(request):
    return render(request, 'page1.html')


def page2_view(request):
    return render(request, 'page2.html')


def page3_view(request):
    return render(request, 'page3.html')

def pagen_view(request, n):
    return render(request, 'pagen.html', locals())















