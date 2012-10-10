from django import forms
from datetime import datetime
import pytz
from pytz import timezone
from bossspawns.deathclock.models import DeathCount

class DeathCountForm(forms.Form):
    death_time = forms.DateTimeField(label='Time of death', initial="Click to enter a time")

    def save(self, user, boss, server):
        if not self.is_valid():
            return None
        death_time = self.cleaned_data['death_time']
        death_count = DeathCount.objects.create(
            user=user,
            boss=boss,
            server=server,
            died_at=death_time
        )
        return death_count
