from django.urls import path

from . import views

urlpatterns = [

    path("",views.hello),
    path("luis",views.luis,name="luis"),
    path("david",views.david,name='david'),
    path("<str:name>",views.greet,name='greet'),
]
