#!/bin/sh

set -o errexit
set -o nounset

# run gunicorn
gunicorn main:app -b 0.0.0.0:8000 --access-logfile '-'

exec "$@"