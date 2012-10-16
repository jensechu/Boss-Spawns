from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from timezones.fields import TimeZoneField

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    timezone = TimeZoneField('your local timezone', default=settings.TIME_ZONE)
