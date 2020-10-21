from django.db import models
from django.conf import settings
from django import forms
from datetime import datetime

class VolunteerEvent(models.Model):

    # tags_choices =[
    #     ('HOME_REPAIR', 'Home Repair'), 
    #     ('BAKE_SALE', 'Bake Sale')
    # ]

    event_title = models.CharField(max_length=25)
    event_datetime = models.DateTimeField(default=datetime(2020, 1, 1))
    event_description = models.CharField(max_length=250)
    # event_tags = models.CharField(max_length=15, choices=tags_choices, null=True, blank=True)
    event_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.event_title