python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn afridemia.wsgi:application --bind 0.0.0.0:8000 --workers 3