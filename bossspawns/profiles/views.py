from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
from bossspawns.profiles.forms import ProfileForm

@login_required
def my_profile(request):
    profile = request.user.get_profile()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid(): 
            messages.success(request, 'Profile details updated.')
            profile_form.save()
            return HttpResponseRedirect(reverse('user-profile'))
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile.html', {
            'profile_form': profile_form
    })
