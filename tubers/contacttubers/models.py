from django.db import models
from datetime import datetime
# Create your models here.
class ContactTubers(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.full_name