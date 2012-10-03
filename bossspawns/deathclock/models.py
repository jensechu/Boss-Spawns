from django.db import models


class Boss(models.Model):
    name = models.CharField(max_length=200)
    respawn_rate = TimeField('respawn time')
    ZONES = (
        ('SF', 'Sparkfly Fen'),
        ('BS', 'Blazeridge Steppes'),
        ('FS', 'Frostgorge Sound')
    )
    boss_location = models.CharField(max_length=200, choices=ZONES)

class DeathCount(models.Model):
    boss = models.ForeignKey(Boss)
    death_time = models.TimeField('time of death')
    SERVERS = (
        ('JQ', 'Jade Quarry'),
        ('DH', 'Dark Haven')
    )
    server = models.CharField(max_length=200, choices=SERVERS)
    

