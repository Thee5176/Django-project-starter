#!/usr/bin/bash

git fetch -f
git reset --hard origin/HEAD

# update excecution for new bash script
chmod +x `ls _script/*.sh`

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py check
