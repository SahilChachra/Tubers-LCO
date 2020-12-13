from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages, auth

def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password) # available to all django templates by default
        # authenticate just checks if user is there in database or not
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Logged in.")
            return redirect("dashboard")

        else:
            messages.error(request, "Invalid credentials.")
            return redirect("login")


    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):

    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username exists!")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email exists")
                    return redirect('resgiter')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully!')
                    return redirect('login')
        else:
            messages.error(request, "Password mismatch")
            return redirect('register')

    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

