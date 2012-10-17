from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Store whatever User.get_profile is when we load this model
user_get_profile = User.get_profile

def get_or_create_profile(user):
    '''
    A wrapper around User.get_profile()
    that creates profiles when they are not found.
    '''
    ProfileModel = models.get_model(*settings.AUTH_PROFILE_MODULE.split('.'))
    try: 
        # Equivalent to user.get_profile()
        # Just passing explicit self to old method
        profile = user_get_profile(user) 
    except ProfileModel.DoesNotExist:
        profile, created = ProfileModel.objects.get_or_create(user=user)

    return profile

# Replace User.get_profile() with a method that tries to create a profile
# if one is not found if we haven't already.  (Like, if this model is loaded 
# multiple times in development, we don't want to patch it again)
if user_get_profile != get_or_create_profile:
    User.get_profile = get_or_create_profile
