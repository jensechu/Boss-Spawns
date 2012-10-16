from django.contrib import admin
from bossspawns.profiles.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'timezone')

admin.site.register(UserProfile, UserProfileAdmin)
