from django.contrib import admin

#new stuff
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from .models import VolunteerEvent
from django.conf import settings


admin.site.register(VolunteerEvent)

#admin.site.register(User)