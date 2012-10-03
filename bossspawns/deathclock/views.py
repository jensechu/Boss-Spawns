from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from deathclock.models import Boss

def home(request):
    bosses = Boss.objects.all()
    return render_to_response('bosses.html', {'boss_list': bosses})

def detail(request, boss_id):
    boss = get_object_or_404(Boss, pk=boss_id)
    return render_to_response('boss_detail.html', {"boss": boss})
    
