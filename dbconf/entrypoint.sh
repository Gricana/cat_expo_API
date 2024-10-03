#!/bin/bash

source /expo/dbconf/db.env

./wait-for-it.sh db:5432 -- echo "Database is up"

python manage.py makemigrations api --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

export PGPASSWORD=$DB_PASSWORD
psql -h db -U $DB_USER -d $DB_NAME -f /expo/dbconf/dump.sql

gunicorn --bind 0.0.0.0:8080 exhibition.wsgi:application
