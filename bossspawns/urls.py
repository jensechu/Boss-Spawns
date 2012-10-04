from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bossspawns.deathclock.views.home', name='home'),
    url(r'^server/$', 'bossspawns.deathclock.views.server'),
    url(r'^server/(?P<server_id>\d+)/$', 'bossspawns.deathclock.views.server', name='server'),
    url(r'^server/(?P<server_id>\d+)/boss/(?P<boss_id>\d+)/$', 'bossspawns.deathclock.views.boss', name='server-boss'),
    url(r'^server/(?P<server_id>\d+)/boss/(?P<boss_id>\d+)/death/$', 'bossspawns.deathclock.views.boss_death', name='boss-death'),

    url(r'^admin/', include(admin.site.urls)),
)
