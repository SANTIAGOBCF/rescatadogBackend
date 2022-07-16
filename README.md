# Quick Install - Python venv
## Python version
`Python 3.10`

## Create a virtual env:
`python3 -m venv zz_env`

Activate virtual env

## Install all dependencies:

`pip install -r requirements.txt`


## Run django server:
`python manage.py runserver`


## Visit the api:
`http://127.0.0.1:8000/api/docs`

## Visit admin:
`http://127.0.0.1:8000/admin`

# Repo config

## Precommit config
`pre-commit install`
`pre-commit install --hook-type commit-msg`


# Quick Install - Docker

## Requerimientos
`Docker 20`

## Variables de entorno
Crear un archivo `.env` en la raiz del proyecto con el siguiente contenido, es un ejemplo:
```dotenv
SECRET_KEY="7g7!_a6$111hv9p-n-8^9bbk3-r)*2_39h8o4fjqb^8p_7t="
DEBUG=True
ENGINE="postgres"
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
POSTGRES_HOST=app_db:5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=rescatadog
DATABASE_PORT="5432"
```

## Build backend
`docker compose build`

## Levantar contenedores
`docker compose up -d`

## Migraciones en base de datos
`docker exec -it rescatadog bash -c "python manage.py migrate"`

## Crear super usuario
`docker exec -it rescatadog bash -c "python manage.py createsuperuser --no-input"`

## Crear archivos estaticos
`docker exec -it rescatadog bash -c "python manage.py collectstatic"`

