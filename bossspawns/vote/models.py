from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.utils.timezone import now

class Vote(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField('Time of vote', default=now)

    content_type = models.ForeignKey(ContentType)
    thing_id = models.PositiveIntegerField()
    thing = generic.GenericForeignKey('content_type', 'thing_id')
