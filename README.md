Boss-Spawns
===========

A user submission based web app that estimates when Guild Wars 2 bosses spawn.

Hosted at http://gw2spawns.herokuapp.com/

### Intial setup

```bash
## Set up the virtualenv
$ virtualenv boss-spawns
$ cd boss-spawns
$ echo 'export DJANGO_SETTINGS_MODULE=bossspawns.settings' >> bin/activate
$ . bin/activate

## Check out the code
$ mkdir src
$ cd src
$ git clone https://github.com/jensechu/Boss-Spawns.git
$ cd Boss-Spawns

## Install the dependencies
$ pip install -r requirements.local.txt

## Setup the db and run the server
$ django-admin.py syncdb --settings=bossspawns.settings
$ django-admin.py runserver --settings=bossspawns.settings
```

Then every time after that you can just activate the environment and go

```bash
$ cd boss-spawns
$ . bin/activate
$ cd src/Boss-Spawns
$ django-admin.py runserver
# [.. Hackin hack hack .. ]
```

### Deploy notes

This app can be deployed to Heroku. It requires that the 'DJANGO_SETTINGS_MODULE' be set
and that the `user-env-compile` setting is on so that the correct settings are loaded during deploy.

To setup a heroku deployment of this app, install the Heroku tools and perform the following steps:

```bash
$ heroku create
$ heroku config:set DJANGO_SETTINGS_MODULE=bossspawns.heroku
$ heroku labs:enable user-env-compile
$ git push heroku master
$ heroku run python manage.py syncdb
# .. And fill out the admin form .. #
$ heroku open
```
