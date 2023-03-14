from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    admin_user = models.ForeignKey("Profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    hours = models.CharField(max_length=150)
    details = models.CharField(max_length=150)
    coordinates = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    venue_image = models.CharField(max_length=150)
    favorite = models.ManyToManyField("Profile", through="favorite", related_name="favorite_venue")
