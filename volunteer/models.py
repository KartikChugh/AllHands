from django.db import models
from django.conf import settings
from django import forms
from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class VolunteerEvent(models.Model):

    # tags_choices =[
    #     ('HOME_REPAIR', 'Home Repair'), 
    #     ('BAKE_SALE', 'Bake Sale')
    # ]

    event_title = models.CharField(max_length=25)
    event_datetime = models.DateTimeField(default=datetime.now())
    event_description = models.CharField(max_length=250)
    # event_tags = models.CharField(max_length=15, choices=tags_choices, null=True, blank=True)
    cover = models.ImageField(upload_to='images/', blank=False, null=False, default="stock/thomas.jpg")
    event_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.event_title

class VolunteerProfile(models.Model):
    #user = models.ManyToManyField(User),
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    eventlist=ArrayField(models.CharField(max_length=20), blank=True)
    numofevents=models.IntegerField(default=0)
    def __str__(self):
        return self.user
