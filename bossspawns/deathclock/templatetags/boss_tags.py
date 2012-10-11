from django import template
from bossspawns.deathclock.models import Server

register = template.Library()

@register.filter
def next_spawn(boss, server):
    return boss.next_spawn(server) or "Unknown"

@register.inclusion_tag('deathclock/server_select.html', takes_context=True)
def server_select(context):
    servers = Server.objects.all()
    selected = context.get('server')
    return {"server_list": servers, 'selected_server': selected}
