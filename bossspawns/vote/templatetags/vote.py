from django import template
from django.contrib.contenttypes.models import ContentType
from bossspawns.vote.models import Vote

register = template.Library()

@register.inclusion_tag('vote/form.html')
def vote_form(thing):
    return {
        "thing": thing,
        "content_type": ContentType.objects.get_for_model(thing)
    }

@register.simple_tag
def vote_count(thing):
    content_type = ContentType.objects.get_for_model(thing)
    return Vote.objects.filter(thing_id=thing.pk, content_type=content_type).count()
