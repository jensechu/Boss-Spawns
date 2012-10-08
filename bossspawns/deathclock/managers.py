from datetime import datetime, timedelta
from django.utils.timezone import now
from django.db import models
from django.db.models.query import QuerySet

class DeathFiltersMixin(object):
    def server(self, server):
        return self.filter(server=server)

    def boss(self, boss):
        return self.filter(boss=boss)

class DeathCountManager(models.Manager, DeathFiltersMixin):
    class DeathQuerySet(QuerySet, DeathFiltersMixin):
        pass

    def get_query_set(self):
        return self.DeathQuerySet(self.model)

    def in_spawn_range(self, boss, server):
        death_qs =  self.boss(boss).server(server)
        limit = now() - timedelta(seconds=boss.respawn_rate)
        limit = limit.astimezone(server.tz)
        return death_qs.filter(died_at__gte=limit)
