from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bossspawns.deathclock.views.home', name='home'),
    url(r'^server/$', 'bossspawns.deathclock.views.server'),
    url(r'^server/(?P<server_id>\d+)/$', 'bossspawns.deathclock.views.server', name='server'),
    url(r'^server/(?P<server_id>\d+)/boss/(?P<boss_id>\d+)/$', 'bossspawns.deathclock.views.boss', name='server-boss'),
    url(r'^server/(?P<server_id>\d+)/boss/(?P<boss_id>\d+)/death/$', 'bossspawns.deathclock.views.boss_death', name='boss-death'),

    url(r'^vote/', include('bossspawns.vote.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

## Static routes. If there's a server catchign these above,
## this route will never get hit
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
