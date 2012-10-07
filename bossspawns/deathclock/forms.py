from django import forms
from datetime import datetime
from pytz import timezone
from bossspawns.deathclock.models import DeathCount

class DeathCountForm(forms.Form):
    death_time = forms.DateTimeField(label='Time of death', initial=datetime.now)

    def save(self, user, boss, server):
        if not self.is_valid():
            return None
        death_time = self.cleaned_data['death_time'].replace(tzinfo=server.tz)
        death_count = DeathCount.objects.create(
            user=user, 
            boss=boss, 
            server=server, 
            died_at=death_time
        )
        return death_count
