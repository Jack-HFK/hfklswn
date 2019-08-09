from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# 导入setting模块
from django.conf import settings
import os


# Create your views here.

# file: index/views.py

def index_view(request):
    return render(request, "index/index.html", locals())


def upload_view(request):
    if request.method == "GET":
        return render(request, "index/upload_file.html", locals())
    elif request.method == "POST":
        # 此时可以通过request.FILES来获取文件
        a_file = request.FILES["myfile"]
        # 此处保存上传的文件到项目文件夹/static/files文件夹内
        # 得到要保存文件的路径
        # 计算出static/files/文件夹位置及文件名字
        filename = os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename,"wb") as f:
            # a_file.file 绑定一个已经代开的文件流对象
            data = a_file.file.read()  # 读取文件
            f.write(data) #　写入文件
            return HttpResponse("文件" + a_file.name + "上传成功")
