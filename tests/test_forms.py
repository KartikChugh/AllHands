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
            form.fields['event_datetime'].label == 'Date and Time')


    def test_create_event_form_event_title_help_text(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_title'].help_text == 'Max Length: 25')

    def test_create_event_form_event_description_label(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_description'].help_text == 'Max Length: 100')


    def test_create_event_form_event_datetime_label(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_datetime'].help_text == 'Format: yyyy-mm-dd hh:mm:ss')




    # def test_renew_form_date_in_past(self):
    #     date = datetime.date.today() - datetime.timedelta(days=1)
    #     form = RenewBookForm(data={'renewal_date': date})
    #     self.assertFalse(form.is_valid())
    #
    # def test_renew_form_date_too_far_in_future(self):
    #     date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
    #     form = RenewBookForm(data={'renewal_date': date})
    #     self.assertFalse(form.is_valid())
    #
    # def test_renew_form_date_today(self):
    #     date = datetime.date.today()
    #     form = RenewBookForm(data={'renewal_date': date})
    #     self.assertTrue(form.is_valid())
    #
    # def test_renew_form_date_max(self):
    #     date = timezone.localtime() + datetime.timedelta(weeks=4)
    #     form = RenewBookForm(data={'renewal_date': date})
    #     self.assertTrue(form.is_valid())