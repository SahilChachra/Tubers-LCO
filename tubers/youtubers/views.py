from django.shortcuts import render, get_object_or_404
from .models import Youtuber
# Create your views here.

def youtubers(request): # for youtubers.html
    tubers = Youtuber.objects.order_by('-created_date')
    print(tubers)
    data = {
        'tubers' : tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request, id): # page for each specific youtuber
    tuber = get_object_or_404(Youtuber, pk = id)
    data = {
        'tuber' : tuber,
    }
    return render(request, 'youtubers/youtuber_detail.html', data)

def search(request):
    
    tubers = Youtuber.objects.order_by('-created_date')

    city_search = Youtuber.objects.values_list('city', flat=True).distinct() # city is field name
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct() # camera is field name
    category_search = Youtuber.objects.values_list('category', flat=True).distinct() # category is field name


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword) # icontains means pur in raipur and jaipur
        
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if city:
            tubers = tubers.filter(camera_type__iexact=camera_type)
    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)


    data = {
        'tubers' : tubers,
        'city_search' : city_search, # to shows list of cities in drop down of search
        'camera_type_search':camera_type_search,
        'category_search' : category_search,

    }
    return render(request, 'youtubers/search.html', data)