from django.db import models
from django.db.models.query import QuerySet

def server_method(self, server):
    return self.filter(server=server)

def boss_method(self, boss):
    return self.filter(boss=boss)

class DeathCountManager(models.Manager):
    class DeathQuerySet(QuerySet):
        server = server_method
        boss = boss_method
    
    def get_query_set(self):
        return self.DeathQuerySet(self.model)

    server = server_method
    boss = boss_method

