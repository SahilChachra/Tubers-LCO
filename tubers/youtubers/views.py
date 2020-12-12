from django.shortcuts import render
from .models import Youtuber
# Create your views here.

def youtubers(request): # for youtubers.html
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers' : tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request, id): # page for each specific youtuber
    pass

def search(request):
    pass