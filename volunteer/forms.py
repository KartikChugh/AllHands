from django import forms
from django.utils import timezone

from .models import VolunteerEvent


class PostForm(forms.ModelForm):
    class Meta:
        model = VolunteerEvent
        fields = ['event_title', 'event_description', 'cover', 'event_datetime', 'event_location']

        labels = {
            'event_title': ('Title'),
            'event_description': ('Description'),
            'cover':('Cover Photo'),
            'event_datetime':('Start Date and Time'),
            'event_location':('Location'),
            # 'tags':('Useful Tags')
        }

        help_texts = {
            'event_title': ('What is your event called?'),
            'event_description':('What will volunteers be doing?'),
            'event_datetime': ('When is your event?'),
            'event_location':('Where is your event?'),
            'cover':('Optional: Add a photo/flyer (1:1 ratio preferred)')
        }
        required = {'cover': ("False") }

    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(PostForm, self).clean()

        # extract the username and text field from the data
        date_entered = self.cleaned_data.get('event_datetime')

        # conditions to be met for the username length
        if date_entered < timezone.now():
            self._errors['event_datetime'] = self.error_class([
                'Please enter a date in the future'])


        # return any errors if found
        return self.cleaned_data