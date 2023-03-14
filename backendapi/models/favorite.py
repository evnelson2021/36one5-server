from django.db import models

class Favorite(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='profile_with_favorite')
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, related_name='favorite_venue')