from django.db import models

class VolunteerEvent(models.Model):
    event_title = models.CharField(max_length=25)
    event_datetime = models.DateTimeField()