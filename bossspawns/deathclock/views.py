from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from deathclock.models import Server, Boss

def home(request):
    servers = Server.objects.all()
    return render_to_response('select_server.html', {'server_list': servers})

def server(request, server_id=None):
    if server_id == None:
        server_id = request.GET.get('server', None)
    server = get_object_or_404(Server, pk=server_id)
    bosses = Boss.objects.all()
    return render_to_response('server_bosses.html', {
            'server': server,
            'bosses': bosses
    })
