#!/bin/sh

set -e

# Collect static files added for each Django application and places them
# in the static file directory which can then be sent to the proxy
# to be served directly.
python ./manage.py collectstatic --noinput

# Run migrations to ensure that database is updated to the latest version.
python ./manage.py makemigrations &&
  python ./manage.py migrate &&
  python ./manage.py runserver 0.0.0.0:8000
