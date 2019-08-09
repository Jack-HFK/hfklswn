"""
file " fiction_books/views.py
"""
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# 模板传参是指把数据形成字典,传参给模板,为模板渲染提供数据
#   使用 render() 直接加载并响应模板
def zhuxian_view(request):
    name3 = "诛仙"
    name4 = 88
    # locals()直接将局部变量组合成字典形式{变量名:值,变量名:值 ... ...}
    return render(request, "temlplates3.html", locals())


# 视图函数中创建模型类记录
from . import models


def models_class(request):
    if request.method == "GET":
        create = models.Fictioc_Books.objects.create(book_name="磨合洛传", book_price=250.00)
        class_name = models.Fictioc_Books()
        class_name.book_name = "诛仙"
        class_name.book_price = 260.55
        class_name.save()


from . import forms

#                                                  此处错误代码
def fiction_books_forms(request):
    if request.method == "GET":
        forms1 = forms.Forms1()
        return render(request,"fiction_books/forms_Form.html",locals())
    elif request.method == "POST":
       # 如何拿到表单数据，实现表单验证
        form = forms.Forms1(request.POST)
        if form.is_valid():
            html = str(form.cleaned_data)
            return HttpResponse(html)
        else:
            return HttpResponse("不合法数据提交")