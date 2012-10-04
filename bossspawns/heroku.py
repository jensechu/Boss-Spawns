from bossspawns.settings import *

## Heroku auto-db config
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
