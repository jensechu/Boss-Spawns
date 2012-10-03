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
    
    def __unicode__(self):
        return self.name

class DeathCount(models.Model):
    """Time intervals for the Boss'"""

    boss = models.ForeignKey(Boss)
    died_at = models.TimeField('time of death')
    server = models.ForeignKey(Server)

    def __unicode__(self):
        return "%s, %s" % (self.boss.name, self.server.name)
