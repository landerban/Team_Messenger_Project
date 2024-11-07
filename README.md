# Messenger

imported

- Django
- chnnels
- websockets
- chnnels_redis

run server (init)

> python manage.py migrate

> python manage.py runserver

run docker for websockets (localhost for now)

> docker run -p 6379:6379 -d redis:5

create admin

> python manage.py createsuperuser

models to db migration

> python manage.py makemigrations
