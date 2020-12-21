from django.contrib import admin
from .models import Hiretubers
# Register your models here.
from django.utils.html import format_html

class HiretuberAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'tuber_name')

admin.site.register(Hiretubers, HiretuberAdmin)
