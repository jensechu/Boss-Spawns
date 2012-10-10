from django import template
from bossspawns.deathclock.models import Server

register = template.Library()

@register.filter
def next_spawn(boss, server):
    return boss.next_spawn(server) or "Unknown"

@register.inclusion_tag('deathclock/server_select.html')
def server_select():
    servers = Server.objects.all()
    return {"server_list": servers}
