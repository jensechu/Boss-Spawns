from django import forms
from datetime import datetime
from bossspawns.deathclock.models import DeathCount

class DeathCountForm(forms.Form):
    death_time = forms.DateTimeField(label='Time of death', initial=datetime.now)

    def save(self, user, boss, server):
        death_count = DeathCount.objects.create(
            user=user, 
            boss=boss, 
            server=server, 
            died_at=self.cleaned_data['death_time']
        )
        return death_count
