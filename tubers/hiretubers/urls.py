from django.urls import path
from . import views

urlpatterns = [
    path('hiretubers', views.hiretubers, name="hiretubers"), #go to views.py and run home() as home url has been called
   
]
