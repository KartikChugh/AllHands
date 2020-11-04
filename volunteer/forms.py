from django import forms
from .models import VolunteerEvent


class PostForm(forms.ModelForm):
    class Meta:
        model = VolunteerEvent
        fields = ['event_title', 'event_description', 'cover', 'event_datetime']

        labels = {
            'event_title': ('Title'),
            'event_description': ('Description'),
            'cover':('Cover Photo'),
            'event_datetime':('Date and Time')
        }

        help_texts = {
            'event_title': ('Max Length: 25'),
            'event_description':('Max Length: 100'),
            'event_datetime': ('Format: yyyy-mm-dd hh:mm:ss')
        }
        required = {'cover': ("False") }
