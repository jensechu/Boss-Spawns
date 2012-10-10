from django.utils.timezone import now
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from bossspawns.deathclock.models import Server, Boss, DeathCount
from bossspawns.deathclock.forms import DeathCountForm

def home(request):
    return render(request, 'index.html', {})

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
            'deaths': DeathCount.objects.in_spawn_range(boss, server),
            'death_form': DeathCountForm,
            'server_time': now().astimezone(server.tz)
    })

@require_POST
@login_required
def boss_death(request, server_id, boss_id):
    server = get_object_or_404(Server, pk=server_id)
    boss = get_object_or_404(Boss, pk=boss_id)
    
    form = DeathCountForm(request.POST)
    if form.is_valid():
        form.save(request.user, boss, server)
        return HttpResponseRedirect(reverse('server-boss', args=[server.pk, boss.pk]))

    return render(request, 'boss_details.html', {
            'server': server,
            'boss': boss,
            'deaths': DeathCount.objects.in_spawn_range(boss, server),
            'death_form': form,
            'server_time': now().astimezone(server.tz)
    })
