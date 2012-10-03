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

class DeathCount(models.Model):
    """ """
    SERVERS = (
        ('JQ', 'Jade Quarry'),
        ('DH', 'Darkhaven')
    )
    boss = models.ForeignKey(Boss)
    time = models.TimeField('time of death')
    server = models.CharField(max_length=5, choices=SERVERS)
