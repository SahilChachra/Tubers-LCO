from django.db import models
from datetime import datetime
# Create your models here.
class Hiretubers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tubers_id = models.IntegerField(blank=True)
    tuber_name = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email