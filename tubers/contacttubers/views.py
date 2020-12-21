from .models import ContactTubers
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
def contacttubers(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']

        # perform checks and all
        ct = ContactTubers(full_name=full_name, phone=phone, email=email, company=company, subject=subject, message=message)
        ct.save()
        messages.success(request, "Thanks for reaching out!")
        return redirect('home')