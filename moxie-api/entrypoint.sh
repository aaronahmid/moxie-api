#!/bin/sh

echo "Running Database Migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000