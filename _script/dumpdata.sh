#!/usr/bin/bash

docker-compose exec web python manage.py migrate

echo "Dumping testdata..."

# Customize 
docker-compose exec web python manage.py dumpdata <app_name>  --indent 4 > _testdata/<file_name>.json

echo "Finish Dumping testdata"