#!/usr/bin/bash

# build and migrate db
docker-compose up -d --build
docker-compose exec web python manage.py migrate