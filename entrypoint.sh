#!/bin/sh
sh -c "python manage.py makemigrations" &&
sh -c "python manage.py migrate" &&
sh -c "gunicorn api_service:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 & gunicorn config.wsgi:application --bind 0.0.0.0:8800"