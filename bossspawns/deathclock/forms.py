from django import forms
from datetime import datetime

class DeathCountForm(forms.Form):
    death_time = forms.DateTimeField(label='Time of death', initial=datetime.now)

