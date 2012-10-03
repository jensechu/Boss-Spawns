from django.contrib import admin
from deathclock.models import Boss, DeathCount

class DeathCountAdmin(admin.ModelAdmin):
    list_display = ('boss', 'server')

admin.site.register(Boss)
admin.site.register(DeathCount, DeathCountAdmin)
