from django.contrib import admin
from .models import ContactTubers
# Register your models here.
from django.utils.html import format_html

class ContactTuberAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'email', 'subject')

admin.site.register(ContactTubers, ContactTuberAdmin)