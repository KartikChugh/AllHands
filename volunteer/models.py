from django.db import models
from django.conf import settings
from django import forms
from datetime import datetime

class VolunteerEvent(models.Model):
    event_title = models.CharField(max_length=25, default=None)
    event_datetime = models.DateTimeField(default=datetime.now())
    event_description = models.CharField(max_length=250, default=None)
    event_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    # event_tags = forms.MultipleChoiceField()

    def __str__(self):
        return self.event_title