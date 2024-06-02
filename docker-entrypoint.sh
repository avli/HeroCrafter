#!/bin/bash

(cd src && poetry run python manage.py migrate --noinput)

echo Starting server...

(cd src && poetry run uwsgi --http :8000 --module core.wsgi)
