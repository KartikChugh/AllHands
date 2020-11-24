import datetime

from django.test import TestCase
from django.utils import timezone

from volunteer.forms import PostForm


class CreateEventFormTest(TestCase):
    def test_create_event_form_event_title_label(self):
        form = PostForm()
        print(form.fields['cover'].required)
        self.assertTrue(
            form.fields['event_title'].label == 'Title')

    def test_create_event_form_event_description_label(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_description'].label == 'Description')

    def test_create_event_form_cover_label(self):
        form = PostForm()
        self.assertTrue(
            form.fields['cover'].label == 'Cover Photo')

    def test_create_event_form_event_datetime_label(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_datetime'].label == 'Start Date and Time:')


    def test_create_event_form_event_title_help_text(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_title'].help_text == 'What is your event called?')

    def test_create_event_form_event_description_label(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_description'].help_text == 'What will volunteers be doing?')


    def test_create_event_form_event_datetime_label(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_datetime'].help_text == 'When is your event?')


