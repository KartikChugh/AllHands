from django.db import models
from django.conf import settings
from django import forms
import datetime

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone

from taggit.managers import  TaggableManager

# Returns a datetime corresponding to tomorrow, 8AM
def get_tomorrow_morning():
    now = datetime.datetime.now()
    tmrw = now + datetime.timedelta(days=1)
    tmrw = tmrw.replace(hour=8, minute=0, second=0, microsecond=0)
    return tmrw

class VolunteerEvent(models.Model):

    event_title = models.CharField(max_length=45)
    event_datetime = models.DateTimeField(default=get_tomorrow_morning)
    event_description = models.CharField(max_length=250)
    event_location = models.CharField(max_length=100, default="Rotunda Steps")
    cover = models.ImageField(upload_to='images/', blank=False, null=False, default="stock/thomas.jpg")
    event_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
        related_name="events_written"
    )
    attending=models.ManyToManyField(User, related_name='events_attending')
    
    TAGGIT_CASE_INSENSITIVE  = True
    tags  = TaggableManager("Tags", "home repair, cooking, yardwork, children, school, technology, political, other")
    #slug=models.SlugField(null=True)
    def __str__(self):
        return self.event_title
    #def get_absolute_url(self):
     #   return reverse('event_detail', kwargs={'slug': self.slug})
    def is_past(self):
        return timezone.now() > self.event_datetime

    

