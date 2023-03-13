from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    hours = models.CharField(max_length=150)
    details = models.CharField(max_length=150)
    coordinates = models.CharField(max_length=150)
