from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def page1_view(request):
    html = "999"
    return HttpResponse(html)