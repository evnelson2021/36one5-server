from django.db import models

class Event(models.Model):
    admin_user = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="admin_user")
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE, related_name="venue")
    name = models.CharField(max_length=150)
    date = models.DecimalField(max_digits=2, decimal_places=1)
    doors = models.IntegerField()
    start_time = models.IntegerField()
    event_type = models.ForeignKey("EventType", on_delete=models.CASCADE, related_name="event_type")
    details = models.CharField(max_length=150)
    ticket_link = models.CharField(max_length=150)
