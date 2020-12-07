from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), #go to views.py and run home() as home url has been called
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
]
