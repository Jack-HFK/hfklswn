from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("运动主页")