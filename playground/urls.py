from django.urls import path 
from .import views 

urlpatterns = [
    path('hello/',views.say_hello),
    path('home/',views.say_home)
]
