from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.inclusion_tag('vote/form.html')
def vote_form(thing):
    return {
        "thing": thing,
        "content_type": ContentType.objects.get_for_model(thing)
    }
