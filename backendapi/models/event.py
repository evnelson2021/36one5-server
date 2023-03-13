from django.db import models

class Event(models.Model):
    # admin_user = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="admin_user")
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE, related_name="event_venue")
    name = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    doors = models.CharField(max_length=150)
    start_time = models.CharField(max_length=150)
    event_type = models.ForeignKey("EventType", on_delete=models.CASCADE, related_name="event_type")
    details = models.CharField(max_length=150)
    ticket_link = models.CharField(max_length=150)
