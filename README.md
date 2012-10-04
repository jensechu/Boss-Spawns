Boss-Spawns
===========

A user submission based web app that estimates when Guild Wars 2 bosses spawn.

### Intial setup

```bash
$ git clone https://github.com/jensechu/Boss-Spawns.git
$ cd Boss-Spawns
$ virtualenv ve
# [.. virtualenv is build ..]
$ . ve/bin/activate
$ pip install -r requirements.local.txt
$ django-admin.py syncdb --settings=bossspawns.settings
$ django-admin.py runserver --settings=bossspawns.settings
```

Then every time after that you can just activate the environment and go

```bash
$ cd Boss-Spawns
$ . ve/bin/activate
# [.. Hackin hack hack .. ]
```

If you're tired of typing settings all the time, you can set the settings module
for a shell session

```bash
$ export DJANGO_SETTINGS_MODULE=bossspawns.settings
```

Or add it to the virtual environment startup, so that it's set when
the enviroment is activated with `. ve/bin/activate`

```bash
$ echo 'export DJANGO_SETTINGS_MODULE=bossspawns.settings' >> ve/bin/activate
```

### Deploy notes

This app can be deployed to Heroku. It requires that the 'DJANGO_SETTINGS_MODULE' be set
and that the `user-env-compile` setting is on so that the correct settings are loaded during deploy.

To setup a heroku deployment of this app, install the Heroku tools and perform the following steps:

```bash
$ heroku create
$ heroku config:set DJANGO_SETTINGS_MODULE=bossspawns.heroku
$ heroku labs:enable user-env-compile
$ git push heroku
$ heroku run python manage.py syncdb
# .. And fill out the admin form .. #
$ heroku open
```
