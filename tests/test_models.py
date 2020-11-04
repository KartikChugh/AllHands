from django.test import TestCase

from volunteer.models import VolunteerEvent
from django.contrib.auth.models import User # Required to assign User as a borrower
from django.utils import timezone
import datetime


class VolunteerEventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

        VolunteerEvent.objects.create(event_title='Fun Event', event_description='This event will be really fun')

    # Methods

    def test_past_event(self):
        datetime_past = timezone.now() - datetime.timedelta(milliseconds=1)
        event = VolunteerEvent(event_title='title', event_description='descr', event_datetime=datetime_past)
        self.assertTrue(event.is_past())

    def test_upcoming_event(self):
        datetime_future = timezone.now() + datetime.timedelta(milliseconds=1)
        event = VolunteerEvent(event_title='title', event_description='descr', event_datetime=datetime_future)
        self.assertFalse(event.is_past())

    # Fields

    def test_event_name_label(self):
        v_event = VolunteerEvent.objects.get(id=1)
        field_label = v_event._meta.get_field('event_title').verbose_name
        self.assertEqual(field_label, 'event title')

    def test_event_description_label(self):
        author=VolunteerEvent.objects.get(id=1)
        field_label = author._meta.get_field('event_description').verbose_name
        self.assertEqual(field_label, 'event description')

    def test_event_name_max_length(self):
        author = VolunteerEvent.objects.get(id=1)
        max_length = author._meta.get_field('event_title').max_length
        self.assertEqual(max_length, 45)

    def test_event_description_max_length(self):
        author = VolunteerEvent.objects.get(id=1)
        max_length = author._meta.get_field('event_description').max_length
        self.assertEqual(max_length, 250)

    def test_default_datetime(self):
        author = VolunteerEvent.objects.get(id=1)
        expected_object_name = timezone.now().date()
        self.assertEqual(expected_object_name, author.event_datetime.date())

    def test_event_fields(self):
        title = 'title'
        description = 'description'
        event = VolunteerEvent(event_title=title, event_description=description)
        self.assertEquals(event.event_title, title)
        self.assertEquals(event.event_description, description)

    def test_event_attending_event_set(self):
        event = VolunteerEvent.objects.filter(event_title='Fun Event').first()
        user1 = User.objects.create_user(username='user1', password='abc')
        user2 = User.objects.create_user(username='user2', password='123')
        event.attending.set([user1.pk, user2.pk])
        self.assertEqual(event.attending.count(), 2)


    def test_string_output(self):
        name = 'Fun Event'
        event = VolunteerEvent.objects.filter(event_title=name).first()
        self.assertEqual(str(event),name)
