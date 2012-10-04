from bossspawns.settings import *

## Real webserver
INSTALLED_APPS += ('gunicorn',)

## Heroku auto-db config
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
