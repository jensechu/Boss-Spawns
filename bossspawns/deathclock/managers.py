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

