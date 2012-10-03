from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'deathclock.views.home', name='home'),
    url(r'^server/$', 'deathclock.views.server'),
    url(r'^server/(?P<server_id>\d+)/$', 'deathclock.views.server', name='server'),

    url(r'^admin/', include(admin.site.urls)),
)
