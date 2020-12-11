from django.contrib import admin
# Register your models here.
from .models import Slider, Team
from django.utils.html import format_html # allows formatting

class TeamAdmin(admin.ModelAdmin):

    def my_photo(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    list_display = ('id', 'my_photo' ,'first_name','role','created_date') # added my_photo func to display image in admin panel
    #to make selected field as clickable
    list_display_links = ('first_name', 'id')
    #to make search
    search_fields = ('first_name', 'role', )
    #to get filter on side
    list_filter = ('role', )

admin.site.register(Slider) # To make the model visible in our admin panel
admin.site.register(Team, TeamAdmin) #resgiter Team model
