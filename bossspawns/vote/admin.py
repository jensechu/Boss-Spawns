from django.contrib import admin
from bossspawns.vote.models import Vote

class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vote, VoteAdmin)
