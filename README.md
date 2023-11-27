# AftertimeBalance_BackEnd

#!!Attertion!!
Full production version with all submodules located in
```commandline
git clone https://github.com/AftertimeINFO/aftertime_prod.git
```


i## Content
* Run locally
  * [Quickstart Windows]()


## Quickstart Windows

### Clone separately (optional)
```commandline If needed 
git clone https://github.com/AftertimeORG/AftertimeBalance_backend.git
cd AftertimeBalance_backend
```

### Install tool (optional)
```commandline
pip install poetry
poetry config virtualenvs.in-project true
poetry config virtualenvs.path .\.venv
```

Install libraries
```commandline
poetry install
```

Initial configuration of project (DEVELOPMENT VERSION, SQLite base)
```commandline
copy ./config/settings/dev_databases.py.temp ./config/settings/dev_databases.py
copy ./.env.dev ./.env
poetry run python manage.py init
```

First run DB configuration
```commandline
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
```

### Run the system (for front)
```commandline
poetry run python manage.py runserver 0.0.0.0:8800
```

### Run the system (for sync api)
```commandline
poetry run python api_service.py 
```


## Quickstart Ubuntu




## Quickstart


