from django.db import models
from django.conf import settings
from django import forms

class VolunteerEvent(models.Model):
    event_title = models.CharField(max_length=25)
    event_datetime = models.DateTimeField()
    event_description = models.CharField(max_length=250)
    event_image = models.ImageField()
    event_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    # event_tags = forms.MultipleChoiceField()

    def __str__(self):
        return self.event_title