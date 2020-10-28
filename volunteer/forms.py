from django import forms
from .models import VolunteerEvent


class PostForm(forms.ModelForm):
    class Meta:
        model = VolunteerEvent
        fields = ['event_title', 'event_description', 'cover', 'event_datetime']