from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect # 调用路由重定向
from . import models
# Create your views here.

def add_book_view(request):
    if request.method == "GET":
        btitle = request.GET.get("title","No Name")
        bpub = request.GET.get("pub","")
        # 方法一 创建一条记录
        models.Book.objects.create(title = btitle,
                                 pub = bpub)
        return HttpResponse("添加成功")

        # # 方法2
        # book = models.Book()  # 创建实例
        # book.title = btitle
        # book.pub = bpub
        # book.price = 99.9
        # import datetime
        # book.pub_date = "2018-08-08"
        # book.save()  # 执行SQL语句
        # return HttpResponse("添加成功！")

        # author = models.Author() # 创建实例
        # author.name = "杜甫"
        # author.age = 66
        # author.email = "dufu@.com"
        # author.save()  # 执行SQL语句
        # return HttpResponse("添加成功")


def books_view(request):
    # 查询Entry实体中所有的数据
    books = models.Book.objects.all()
    # 列出所有满足某一个条件的书
    # books = models.Book.objects.filter(pub = "中华")
    # 列出所有满足某两个条件的书
    # books = models.Book.objects.filter(pub = "条件１",title = "条件２")
    return render(request,"bookstore/books.html",locals())

def book_add2_view(request):
    if request.method == "GET":
        return render(request,"bookstore/bookinfo.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        pub = request.POST.get("pub")
        price = request.POST.get("price")
        market_price = request.POST.get("market_price")
        try:
            abook = models.Book.objects.create(
                title=title,
                pub = pub,
                price = price,
                market_price = market_price)
            # HttpResponseRedirect路由重定向
            return HttpResponseRedirect("/bookstore/books")
        except:
            return HttpResponse("添加失败")
