from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from bossspawns.deathclock.models import Server, Boss, DeathCount
from bossspawns.deathclock.forms import DeathCountForm

def home(request):
    servers = Server.objects.all()
    return render(request, 'select_server.html', {'server_list': servers})

def server(request, server_id=None):
    if server_id == None:
        server_id = request.GET.get('server', None)
    server = get_object_or_404(Server, pk=server_id)
    bosses = Boss.objects.all()
    return render(request, 'server_bosses.html', {
            'server': server,
            'bosses': bosses
    })

def boss(request, server_id, boss_id):
    server = get_object_or_404(Server, pk=server_id)
    boss = get_object_or_404(Boss, pk=boss_id)
    return render(request, 'boss_details.html', {
            'server': server,
            'boss': boss,
            'death_form': DeathCountForm
    })

@require_POST
@login_required
def boss_death(request, server_id, boss_id):
    print request.POST
    server = get_object_or_404(Server, pk=server_id)
    boss = get_object_or_404(Boss, pk=boss_id)
    
    form = DeathCountForm(request.POST)
    if form.is_valid():
        death_count = DeathCount.objects.create(
            user=request.user, 
            boss=boss, 
            server=server, 
            died_at=form.cleaned_data['death_time']
        )
        
        return HttpResponseRedirect(reverse('server-boss', args=[server.pk, boss.pk]))

    return render(request, 'boss_details.html', {
            'server': server,
            'boss': boss,
            'death_form': form
    })
