from django.test import TestCase
from .models import VolunteerEvent

class VolunteerEventModelTests(TestCase):
    def test_event_fields(self):
        title = 'title'
        description = 'description'
        event = VolunteerEvent(event_title=title, event_description=description)
        self.assertEquals(event.event_title, title)
        self.assertEquals(event.event_description, description)

class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
    
    def test_dummy_test_case(self):
        self.assertEqual(1, 1)