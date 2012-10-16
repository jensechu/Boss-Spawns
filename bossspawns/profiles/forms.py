from django.forms import ModelForm
from bossspawns.profiles.models import UserProfile

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user')
