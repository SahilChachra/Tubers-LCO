from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"), 
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"), # views.logout is inbuilt in Django. It's keyword. avoid using it
    path('dashboard', views.dashboard, name="dashboard"),
]
