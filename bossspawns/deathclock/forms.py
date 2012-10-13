from datetime import datetime
import pytz
from pytz import timezone
from django.forms.util import ErrorList
from django.utils.timezone import now

from django import forms
from django.contrib.contenttypes.models import ContentType

from bossspawns.deathclock.models import DeathCount
from bossspawns.vote.models import Vote

class DeathCountForm(forms.Form):
    death_time = forms.DateTimeField(label='In server time:', initial="Click to enter a time")

    def save(self, user, boss, server):
        if not self.is_valid():
            return None
        death_time = self.cleaned_data['death_time']
        
        if death_time > now().astimezone(server.tz):
            errors = self._errors.setdefault("death_time", ErrorList())
            errors.append(u"You can't submit a death in the future.")
            return None
            
        death_count, created = DeathCount.objects.get_or_create(
            boss=boss,
            server=server,
            died_at=death_time,

            ## Create params
            defaults={'user': user}

        )
        ## Always vote for your own submission
        ## TODO: Refactor into vote manager
        content_type = ContentType.objects.get_for_model(death_count)
        Vote.objects.get_or_create(user=user, content_type=content_type, thing_id=death_count.pk)

        return death_count
