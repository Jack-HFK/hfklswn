"""
视图处理函数 ： request接受请求:代表的浏览器给我们的数据
             return 响应内容
            一个视图处理函数可以对应多个url路由
            一个utl路由只能对应一个视图处理函数
"""
from django.http import HttpResponse

# 视图处理函数
def index_view(request):
    html = "欢迎来到主页面"
    html += "<a href='/page1'> 第一页 </a>"
    html += "<a href='/page2'> 第二页 </a>"
    html += "<a href='/page3'> 第三页 </a>"
    return HttpResponse(html)

def page1_view(request):
    html = "欢迎来到第一个页面"
    html += "<a href='http://www.tmooc.cn'> 达内 </a>"
    html += "<a href='/page2'> 第二页 </a>"
    html += "<a href='/page3'> 第三页 </a>"
    return HttpResponse(html)

def page2_view(request):
    html = "欢迎来到第二个页面"
    html += "<a href='/'> 返回首页 </a>"
    html += "<a href='/page1'> 第一页 </a>"
    html += "<a href='/page3'> 第三页 </a>"
    return HttpResponse(html)

def page3_view(request):
    html = "欢迎来到第三个页面"
    html += "<a href='/'> 返回首页 </a>"
    html += "<a href='/page1'> 第一页 </a>"
    html += "<a href='/page2'> 第二页 </a>"
    return HttpResponse(html)

# 在视图函数内,可以用正则表达式分组 () 提取参数后用函数位置传参传递给视图函数
def year_view(request,y):
    html = "year中的年份是" + y
    html += "URL路由字符串" + request.path_info
    return HttpResponse(html)


def cal_view(request,a,op,b):
    html = "欢迎来到cal页面"
    a = int(a)
    b = int(b)
    if op == "add":
        ab = a+b
    elif op == "sub":
        ab = a - b
    elif op == "mul":
        ab = a * b
    else:
        return HttpResponse("不能运算")
    return HttpResponse(ab)

def date_viem(request,y,m,d):
    """ y,m,d ： 年 月 日"""
    html = y + "年" + m + "月" + d + "日"
    return HttpResponse(html)

# def date_viem(request,**kwargs):
#     """ y,m,d ： 年 月 日"""
#     html = y + "年" + m + "月" + d + "日"
#     return HttpResponse(html)

def show_info_view(request):
    html = "request.path=" + request.path   # path：只代表URL中的路由
    if request.method == "GET":     #字符串,表示HTTP请求方法,常用值: 'GET' 、 'POST'
        html += "<h4>您正在进行GET请求</h4>"
    elif request.metchod == "POST":
        html += "<h4>您正在进行POST请求</h4>"
    html += "<h5> 您的IP地址是" + request.META["REMOTE_ADDR"]  #客户端IP地址
    html += "<h5> 请求源IP地址是" + request.META['HTTP_REFERER']  #请求源地址
    return HttpResponse(html)

def page_view(request):
    html = ""
    # 字符串,表示 HTTP 请求方法,常用值: 'GET' 、 'POST'
    if request.method == "GET":
        dic = dict(request.GET)   # request.GET获取请求内容
        s = str(dic)
        html = "GET请求：" + s
        get_one = request.GET.get("某个请求值")   # request.GET.get获取GET请求内容中具体某一个请求数据
        gets  = request.GET.getlist("请求列表")   # request.GET.getlist 获取GET请求列表：列表中可以有一个或多个请求
    elif request.method == "POST":
        pass
    return HttpResponse(html)

def sum_view(request,):
    html = ""
    if request.method == "GET":
        start = int(request.GET.get("start"))     # request.GET.get获取GET请求内容中具体某个请求数据
        stop = int(request.GET.get("stop"))
        step = int(request.GET.get("step"))
        html += str(sum(range(start,stop,step)))
    elif request.method == "POST":
        html = "没法计算"
    return HttpResponse(html)

