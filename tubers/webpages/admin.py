from django.contrib import admin
# Register your models here.
from .models import Slider, Team

admin.site.register(Slider) # To make the model visible in our admin panel
admin.site.register(Team) #resgiter Team model