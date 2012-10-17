from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from timezones.fields import TimeZoneField
from django.utils.timezone import now

## Import the app-local patches.py file
import patches


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    timezone = TimeZoneField('your local timezone', default=settings.TIME_ZONE)
