from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request,"hello/index.html")

def luis(request):
    return HttpResponse("Hello,Luis")

def david(request):
    return HttpResponse("Hello,David")

def greet(request,name):
    return render(request,"hello/greet.html",{
        'name': name.capitalize()
    })
