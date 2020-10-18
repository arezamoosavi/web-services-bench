#!/bin/sh

set -o errexit
set -o nounset

python manage.py collectstatic --noinput
uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --reload
