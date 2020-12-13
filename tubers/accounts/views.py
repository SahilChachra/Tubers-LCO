from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def logout_user(request):
    pass

def register(request):
    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

