import datetime

from django.test import TestCase
from django.test import Client
from django.utils import timezone
from volunteer.models import VolunteerEvent
from django.contrib.auth.models import User # Required to assign User as a borrower
from django.urls import reverse


from volunteer.forms import PostForm


class CreateEventFormTestBehavior(TestCase):
    @classmethod
    def setUpTestData(cls):
        now = datetime.datetime.now()
        tmrw = now + datetime.timedelta(days=1)
        tmrw = tmrw.replace(hour=8, minute=0, second=0, microsecond=0)

    def setUp(self):
        user1 = User.objects.create_user("Juliana1," "juliana@dev.ioa", "sopass")
        user1.save()
        self.client.force_login(user=user1)

    def get_tomorrow(self):
        now = datetime.datetime.now()
        tmrw = now + datetime.timedelta(days=1)
        tmrw = tmrw.replace(hour=8, minute=0, second=0, microsecond=0)
        return tmrw

    def get_yesterday(self):
        now = datetime.datetime.now()
        ystr = now - datetime.timedelta(days=1)
        ystr = ystr.replace(hour=8, minute=0, second=0, microsecond=0)
        return ystr

    def test_form_valid(self):
        form_params = {
            'event_title': 'title',
            'event_description': 'description',
            'cover': "stock/thomas.jpg",
            'event_datetime': self.get_tomorrow(),
            'event_location': 'somewhere',
            'tags': 'home repair'
                        }
        response = self.client.post('/volunteer/post/', form_params)
        self.assertEqual(response.status_code, 302)

    def test_form_future_datetime(self):
        form_params = {
            'event_title': 'title',
            'event_description': 'description',
            'cover': "stock/thomas.jpg",
            'event_datetime': self.get_tomorrow(),
            'event_location': 'somewhere',
            'tags': 'home repair'
                        }
        response = self.client.post('/volunteer/post/', form_params)
        self.assertEqual(response.status_code, 302)

    def test_form_present_date(self):
        form_params = {
            'event_title': 'title',
            'event_description': 'description',
            'cover': "stock/thomas.jpg",
            'event_datetime': datetime.datetime.now(),
            'event_location': 'somewhere',
            'tags': 'home repair'
                        }
        response = self.client.post('/volunteer/post/', form_params)
        self.assertEqual(response.status_code, 200)

    def test_form_past_date(self):
        form_params = {
            'event_title': 'title',
            'event_description': 'description',
            'cover': "stock/thomas.jpg",
            'event_datetime': self.get_yesterday(),
            'event_location': 'somewhere',
            'tags': 'home repair'
                        }
        response = self.client.post('/volunteer/post/', form_params)
        self.assertEqual(response.status_code, 200)

    def test_form_missing_title(self):
        form_params = {

            'event_description': 'description',
            'cover': "stock/thomas.jpg",
            'event_datetime': self.get_tomorrow(),
            'event_location': 'somewhere',
            'tags': 'home repair'
                        }
        response = self.client.post('/volunteer/post/', form_params)
        self.assertEqual(response.status_code, 200)

    def test_form_missing_description(self):
        form_params = {
            'event_title': 'title',
            'cover': "stock/thomas.jpg",
            'event_datetime': self.get_tomorrow(),
            'event_location': 'somewhere',
            'tags': 'home repair'
                        }
        response = self.client.post('/volunteer/post/', form_params)
        self.assertEqual(response.status_code, 200)

    def test_form_missing_image(self):
        form_params = {
            'event_title': 'title',
            'event_description': 'description',
            'event_datetime': self.get_tomorrow(),
            'event_location': 'somewhere',
            'tags': 'home repair'
                        }
        response = self.client.post('/volunteer/post/', form_params)
        self.assertEqual(response.status_code, 302)


    def test_form_missing_location(self):
        form_params = {
            'event_title': 'title',
            'event_description': 'description',
            'cover': "stock/thomas.jpg",
            'event_datetime': self.get_tomorrow(),
            'tags': 'home repair'
                        }
        response = self.client.post('/volunteer/post/', form_params)
        self.assertEqual(response.status_code, 200)

    def test_form_missing_tags(self):
        form_params = {
            'event_title': 'title',
            'event_description': 'description',
            'cover': "stock/thomas.jpg",
            'event_datetime': self.get_tomorrow(),
            'event_location': 'somewhere',
                        }
        response = self.client.post('/volunteer/post/', form_params)
        self.assertEqual(response.status_code, 200)

class CreateEventFormTestLabels(TestCase):
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
            form.fields['event_datetime'].label == 'Start Date and Time')


class CreateEventFormTestHelpTexts(TestCase):
    def test_create_event_form_event_title_help_text(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_title'].help_text == 'What is your event called?')

    def test_create_event_form_event_description_help_text(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_description'].help_text == 'What will volunteers be doing?')


    def test_create_event_form_event_datetime_help_text(self):
        form = PostForm()
        self.assertTrue(
            form.fields['event_datetime'].help_text == 'When is your event?')



