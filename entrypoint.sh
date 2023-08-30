#!/bin/sh
python3 -m venv env
bash env/script/activate
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn afridemia.wsgi:application --bind 0.0.0.0:8000 --workers 3