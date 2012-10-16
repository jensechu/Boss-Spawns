from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required
def my_profile(request):
    
    return render(request, 'profiles/profile.html', {})
