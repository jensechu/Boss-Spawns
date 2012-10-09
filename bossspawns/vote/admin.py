from django.contrib import admin
from bossspawns.vote.models import Vote

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'thing', 'created_at')

admin.site.register(Vote, VoteAdmin)
