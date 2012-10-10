from datetime import datetime, timedelta
from django.utils.timezone import now
from django.db import models
from django.db.models.query import QuerySet
import pytz

class DeathFiltersMixin(object):
    def server(self, server):
        return self.filter(server=server)

    def boss(self, boss):
        return self.filter(boss=boss)

class DeathCountManager(models.Manager, DeathFiltersMixin):
    class DeathQuerySet(QuerySet, DeathFiltersMixin):
        def by_vote(self):
            def key(death_count):
                return death_count.votes.count()
            return sorted(self, key=key, reverse=True)

    def get_query_set(self):
        return self.DeathQuerySet(self.model)

    def in_spawn_range(self, boss, server):
        past_buffer = 60 * 10
        death_qs =  self.boss(boss).server(server)
        limit = now() - timedelta(seconds=boss.respawn_rate + past_buffer)
        limit = limit.astimezone(pytz.utc)
        return death_qs.filter(died_at__gte=limit)
