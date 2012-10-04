from django.forms import ModelForm
from bossspawns.deathclock.models import DeathCount

class DeathCountForm(ModelForm):
    class Meta:
        model = DeathCount
