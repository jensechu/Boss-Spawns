from datetime import timedelta
from django.contrib.auth.models import User
from django.db import models
from timezones.fields import TimeZoneField

class Server(models.Model):
    """Guild Wars 2 Server"""
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
        try:
            death_time = DeathCount.objects.server(server).boss(self).latest()

        except DeathCount.DoesNotExist:
            return None
        
        delta = timedelta(seconds=self.respawn_rate)

        return death_time.died_at + delta
    
    def __unicode__(self):
        return self.name

from bossspawns.deathclock.managers import DeathCountManager
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

    def __unicode__(self):
        return "%s, %s" % (self.boss.name, self.server.name)
