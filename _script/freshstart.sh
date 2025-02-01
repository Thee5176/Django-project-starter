#!/usr/bin/bash

# fetch latest change from github
./_script/fetch.sh

# save transaction list
echo "Start backup data..."

mkdir temp/
docker-compose exec web python manage.py dumpdata --indent 4 > temp/backup.json

echo "Finish backup data"

# clear volume and rebuild container
docker-compose down
docker volume rm $(docker volume ls -q)
docker-compose up -d --build
docker-compose exec web python manage.py migrate

# load testdata then temp data

./_script/loaddata.sh

echo "Start Load data"

docker-compose exec web python manage.py loaddata temp/backup.json
rm -rf temp/

echo "Finish Load data"