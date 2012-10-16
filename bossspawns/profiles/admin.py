from django.contrib import admin
from bossspawns.profiles.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')

admin.site.register(UserProfile, UserProfileAdmin)
