from django.contrib import admin

#new stuff
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import VolunteerProfile

from .models import VolunteerEvent
from django.conf import settings


admin.site.register(VolunteerEvent)

class VolunteerProfileInline(admin.StackedInline):
    model=VolunteerProfile
    can_delete=False
    verbose_name_plural='VolunteerProfile'

class UserAdmin(BaseUserAdmin):
    inlines = (VolunteerProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)