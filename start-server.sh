#!/usr/bin/env bash
# start-server.sh
# if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    # (python manage.py createsuperuser --no-input;)
# fi
gunicorn rescatadog.wsgi --reload --user www-data --bind 0.0.0.0:8010 --workers 3 &
nginx -g "daemon off;"
# gunicorn rescatadog.wsgi --user www-data --bind 0.0.0.0:8020 --workers 3
