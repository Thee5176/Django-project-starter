#!/usr/bin/bash

docker-compose exec web python manage.py migrate

echo "Loading testdata..."

docker-compose exec web python manage.py loaddata `ls _testdata/*.json`

echo "Finish Load testdata"