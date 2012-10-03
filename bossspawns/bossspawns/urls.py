from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'deathclock.views.home', name='home'),
    url(r'^boss/(?P<boss_id>\d+)/$', 'deathclock.views.detail', name='details'),
    # url(r'^bossspawns/', include('bossspawns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
