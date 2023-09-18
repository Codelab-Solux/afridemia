#!/bin/sh

set -e 
python manage.py wait_for_db
python manage.py collectstatic --no-input
python manage.py migrate
gunicorn afridemia.wsgi:application --bind 0.0.0.0:8000 --workers 4