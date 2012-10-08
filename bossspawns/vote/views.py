from django.http import HttpResponseRedirect, Http404
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from bossspawns.vote.models import Vote

@require_POST
@login_required
def vote(request):
    content_type = request.POST.get("content_type", "").split(".")
    try:
        content_type = ContentType.objects.get_by_natural_key(*content_type)
    except ContentType.DoesNotExist:
        raise Http404
    thing_id = request.POST.get("thing_id", "0")
    thing = get_object_or_404(content_type.model_class(), pk=thing_id)

    Vote.objects.get_or_create(user=request.user, content_type=content_type, thing_id=thing.pk)

    referer = request.META.get('HTTP_REFERER', "/")
    return HttpResponseRedirect(referer)
    
    
