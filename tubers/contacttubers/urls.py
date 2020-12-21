from django.urls import path
from . import views

urlpatterns = [
    path('contacttubers', views.contacttubers, name="contacttubers"), #go to views.py and run home() as home url has been called
   
]