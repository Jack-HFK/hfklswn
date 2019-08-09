# 调用模块使用 render() 直接加载并响应模板
from django.shortcuts import render



def page0_view(request):
    return render(request,"page_0.html")

def page1_view(request):
    return render(request,"page_1.html")

def page2_view(request):
    return render(request,"page_2.html")

def page3_view(request):
    return render(request,"page_3.html")