#!/bin/sh

echo "Running Database Migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.1:8000