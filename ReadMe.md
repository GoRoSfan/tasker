# Tasker


##Setup

~~~
docker-compose build
docker-compose up
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py create superuser
docker-compose exec web python makemigrations
docker-compose exec web python manage.py migrate
~~~