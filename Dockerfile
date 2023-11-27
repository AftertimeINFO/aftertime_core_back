FROM python:3.10-slim

ENV POETRY_VIRTUALENVS_CREATE=false
# ARG DJANGO_SETTINGS_MODULE
# ENV DJANGO_SETTINGS_MODULE $DJANGO_SETTINGS_MODULE
# RUN echo "Variable is" %DJANGO_SETTINGS_MODULE%

RUN mkdir /app
#
WORKDIR /app
#
COPY poetry.lock .
COPY pyproject.toml .
# Need for psycopg2
RUN apt-get update
RUN apt-get -y install libpq-dev gcc
# Poetry installation
RUN pip install --upgrade pip
RUN pip install poetry
# Poetry configuration
#RUN poetry config virtualenvs.in-project true
#RUN poetry config virtualenvs.path .\.venv
RUN poetry install --no-root
RUN pip install gunicorn

COPY . .
CMD ["sh","./entrypoint.sh"]
# RUN ./run.sh
# CMD ["sh","-c","run.sh"]

# RUN python manage.py makemigrations
# RUN python manage.py migrate
# CMD ["sh"]
# CMD gunicorn api_service:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:9000
# ENTRYPOINT ["sh", "-c"]

# CMD sh -c gunicorn api_service:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 & python manage.py runserver 0.0.0.0:8800 & wait -n
# CMD ["sh", "-c", "gunicorn api_service:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 & gunicorn config.wsgi:application --bind 0.0.0.0:8800"]

# CMD gunicorn config.wsgi:application --bind 0.0.0.0:8800
# CMD python manage.py runserver
# CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8800 & "]
# CMD ["sh", "-c", "gunicorn api_service:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000"]
# CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:9000; gunicorn api_service:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000"]
# CMD ["sh", "-c", "executable_first arg1; executable_second"]