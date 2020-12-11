from django.contrib import admin
# Register your models here.
from .models import Slider, Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','role','created_date')

    #to make selected field as clickable
    list_display_link = ('first_name', 'id')

    #to make search
    search_fields = ('first_name', 'role', )

    #to get filter on side
    list_filter = ('role', )

admin.site.register(Slider) # To make the model visible in our admin panel
admin.site.register(Team, TeamAdmin) #resgiter Team model
