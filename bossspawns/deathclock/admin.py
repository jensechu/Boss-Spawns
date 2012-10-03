from django.contrib import admin
from deathclock.models import Server, Zone, Boss, DeathCount

class DeathCountAdmin(admin.ModelAdmin):
    list_display = ('boss', 'server')

for model in (Server, Zone, Boss):
    admin.site.register(model)

admin.site.register(DeathCount, DeathCountAdmin)
