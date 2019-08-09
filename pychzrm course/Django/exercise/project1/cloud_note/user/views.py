from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def login_views(request):
    return render(request,"user/login.html",locals())

