from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
         url(r'^$', 'bossspawns.profiles.views.my_profile', name='user-profile'),
)
