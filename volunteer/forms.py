from django import forms
from .models import VolunteerEvent


class PostForm(forms.ModelForm):
    class Meta:
        model = VolunteerEvent
        fields = ['event_title', 'event_description', 'cover', 'event_datetime', 'event_location', 'tags']

        labels = {
            'event_title': ('Title'),
            'event_description': ('Description'),
            'cover':('Cover Photo'),
            'event_datetime':('Start Date and Time'),
            'event_location':('Location'),
            'tags':('Useful Tags')
        }

        help_texts = {
            'event_title': ('What is your event called?'),
            'event_description':('What will volunteers be doing?'),
            'event_datetime': ('Format: yyyy-mm-dd hh:mm:ss'),
            'event_location':('Where is your event?'),
            'cover':('Add a photo/flyer (optional)')
        }
        required = {'cover': ("False") }
