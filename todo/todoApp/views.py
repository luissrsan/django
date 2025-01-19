from django.shortcuts import render

# Create your views here.
from . import views

def index(request):
    return render(request,'todoApp/initial.html')


def add(request):
    return render(request,"todoApp/add.html")