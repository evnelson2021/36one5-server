from django.db import models

class Venue(models.Model):
    admin_user = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="admin_user")
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    hours = models.CharField(max_length=150)
    details = models.CharField(max_length=150)
    coordinates = models.CharField(max_length=150)
