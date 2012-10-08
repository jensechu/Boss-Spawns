from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
         url(r'^vote/$', 'bossspawns.vote.views.vote', name='submit-vote'),              
)
