from datetime import timedelta
from django.db import models

class Server(models.Model):
    """Guild Wars 2 Server"""
    name = models.CharField(max_length=50)

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
        death_time = DeathCount.objects.filter(boss=self, server=server)
        try:
            death_time = death_time.latest('died_at')
        except DeathCount.DoesNotExist:
            return None
        
        delta = timedelta(seconds=self.respawn_rate)

        return death_time.died_at + delta
    
    def __unicode__(self):
        return self.name

class DeathCount(models.Model):
    """Time intervals for the Boss'"""

    boss = models.ForeignKey(Boss)
    died_at = models.DateTimeField('time of death')
    server = models.ForeignKey(Server)

    def __unicode__(self):
        return "%s, %s" % (self.boss.name, self.server.name)
