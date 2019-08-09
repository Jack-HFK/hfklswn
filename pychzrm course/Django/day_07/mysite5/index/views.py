from django.shortcuts import render

# Create your views here.

# file: index/views.py

def index_view(request):
    return render(request,"index/index.html",locals())