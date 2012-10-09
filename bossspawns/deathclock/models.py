from datetime import timedelta, datetime
from pytz import timezone
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.db import models
from timezones.fields import TimeZoneField
from bossspawns.deathclock.managers import DeathCountManager
from bossspawns.vote.models import Vote

TZ = timezone(settings.TIME_ZONE)

class Server(models.Model):
    """Guild Wars 2 Server"""
    class Meta:
        ordering = ['name']
        
    name = models.CharField(max_length=50)
    tz = TimeZoneField('server time zone')
    
    def __unicode__(self):
        return self.name

class Zone(models.Model):
    """Guild Wars 2 Zone"""
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Boss(models.Model):
    """Object for an individual boss."""

    name = models.CharField(max_length=200)
    respawn_rate = models.IntegerField('respawn rate in seconds') 
    zone = models.ForeignKey(Zone)

    def next_spawn(self, server):
        deaths = DeathCount.objects.in_spawn_range(self, server)
        death = deaths.by_vote()
        if len(death) == 0:
            return None
        else:
            death = death[0]
        return death.died_at + timedelta(seconds=self.respawn_rate)

    def __unicode__(self):
        return self.name


class DeathCount(models.Model):
    """Time intervals for the Boss'"""
    
    class Meta: 
        ordering = ['-died_at']
        get_latest_by = "died_at"

    objects = DeathCountManager()

    boss = models.ForeignKey(Boss)
    died_at = models.DateTimeField('time of death')
    server = models.ForeignKey(Server)
    user = models.ForeignKey(User)

    votes = generic.GenericRelation(Vote, object_id_field='thing_id')

    def server_death_time(self):
        return self.died_at.replace(tzinfo=self.server.tz)

    def __unicode__(self):
        return "%s, %s" % (self.boss.name, self.server.name)
