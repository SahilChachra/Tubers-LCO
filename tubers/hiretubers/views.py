from django.shortcuts import render
from .models import Hiretubers
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
    
def hiretubers(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tubers_id = request.POST['tuber_id']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']
        email = request.POST['email']

        hiretubers = Hiretubers(first_name=first_name, last_name=last_name, tubers_id=tubers_id, city=city, 
        phone=phone, state=state, message=message, user_id=user_id, email=email)
        hiretubers.save()
        messages.success(request, 'Thanks for reaching us!')
        return redirect('youtubers')