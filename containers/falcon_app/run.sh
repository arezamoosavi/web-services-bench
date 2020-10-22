#!/bin/sh

set -o errexit
set -o nounset

gunicorn main:app -b 0.0.0.0:8000 --reload --access-logfile '-'

exec "$@"