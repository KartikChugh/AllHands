from django.db import models

class VolunteerEvent:
    event_title = models.CharField(max_length=25)
    event_datetime = models.DateTimeField()