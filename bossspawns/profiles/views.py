from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from bossspawns.profiles.forms import ProfileForm

@login_required
def my_profile(request):
    profile = request.user.get_profile()
    profile_form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile.html', {
            'profile_form': profile_form
    })
