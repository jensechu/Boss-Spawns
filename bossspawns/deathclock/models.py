from django.db import models


class Boss(models.Model):
    """ Object for an individual boss."""
    ZONES = (
        ('SF', 'Sparkfly Fen'),
        ('BS', 'Blazeridge Steppes'),
        ('FS', 'Frostgorge Sound')
    )
    name = models.CharField(max_length=200)
    respawn_rate = models.TimeField('respawn rate') 
    location = models.CharField(max_length=5, choices=ZONES)
    
    def __unicode__(self):
        return self.name

class DeathCount(models.Model):
    """ Time intervals for the Boss' """
    SERVERS = (
        ('JQ', 'Jade Quarry'),
        ('DH', 'Darkhaven'),
        ('FtA', 'Fort Aspenwood')
    )
    boss = models.ForeignKey(Boss)
    time = models.TimeField('time of death')
    server = models.CharField(max_length=5, choices=SERVERS)

    def __unicode__(self):
        return "%s, %s" % (self.boss.name, self.get_server_display())
