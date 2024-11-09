# Messenger

Instructions for Frontend

Install node from the website

> https://nodejs.org/en

Check the node version

> node -v

Locate the file and go into it

> cd C:\correct_path\Messenger-app

Install the necessary dependencie

> npm install

Run the dev mode server

> npm run dev

Click on the link

Instructions for Backend

imported

- Django
- channels
- websockets
- channels_redis
- djangorestframework
- django-cors-headers
- daphne


Download Python

> [Go to the official Python website.](https://www.python.org/downloads/)

- Run the downloaded installer.
  > check the box that says "Add Python to PATH"

Check python and pip version

> python --version
> pip --version

Install packages
> pip install django channels djangorestframework django-cors-headers channels_redis daphne

run server (init)

> python manage.py migrate

> python manage.py runserver

run docker for websockets (localhost for now)

> docker run -p 6379:6379 -d redis:5

create admin

> python manage.py createsuperuser

models to db migration

> python manage.py makemigrations
