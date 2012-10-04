from django import template

register = template.Library()

@register.filter
def next_spawn(boss, server):
    return boss.next_spawn(server) or "Unknown"
