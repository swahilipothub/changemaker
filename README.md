# [Django Dashboard DattaAble](https://appseed.us/admin-dashboards/django-dashboard-dattaable)

> **Open-Source Admin Dashboard** coded in **Django Framework** by **AppSeed** [Web App Generator](https://appseed.us/app-generator) - features:

- UI Kit: **DattaAble Dashboard** (Free version) provided by **CodedThemes**
- Codebase: [Django Dashboard Boilerplate](https://github.com/app-generator/boilerplate-code-django-dashboard) v1.0.1
- UI-Ready app, SQLite Database, Django Native ORM
- Modular design, clean code-base
- Session-Based Authentication, Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx
- **MIT License**
- Free support via **Github** 
- Paid Support **24/7 LIVE Support** via [Discord](https://discord.gg/fZC6hup)

> Links

- [Django Dashboard DattaAble](https://appseed.us/admin-dashboards/django-dashboard-dattaable) - Product page
- [Django Dashboard DattaAble](https://django-dashboard-dattaable.appseed.us/login/) - LIVE Demo
- More [Django Admin Dashboards](https://appseed.us/admin-dashboards/django) - index hosted by **AppSeed**
- [Free Admin Dashboards](https://appseed.us/admin-dashboards/open-source) - index hosted by **AppSeed**

<br />

## Want more? Go PRO!

PRO versions include **Premium UI Kits**, Lifetime updates and **24/7 LIVE Support** (via [Discord](https://discord.gg/fZC6hup))

| [Django DattaAble Dark PRO](https://appseed.us/admin-dashboards/django-dashboard-dattaable-dark-pro) | [Django Dashboard Black PRO](https://appseed.us/admin-dashboards/django-dashboard-black-pro) | [Django StarAdmin Dark PRO](https://appseed.us/admin-dashboards/django-dashboard-staradmin-black-pro) |
| --- | --- | --- |
| [![Django DattaAble Dark PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-dattaable-dark-pro/master/media/django-dashboard-dattaable-dark-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-dattaable-dark-pro) | [![Django Dashboard Black PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-black-pro/master/media/django-dashboard-black-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-black-pro) | [![Django StarAdmin Dark PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-staradmin-black-pro/master/media/django-dashboard-staradmin-black-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-staradmin-black-pro)

<br />
<br />

![Django Dashboard DattaAble - Open-Source Admin Panel Coded in Django.](https://raw.githubusercontent.com/app-generator/static/master/django-dashboard-dattaable/django-dashboard-dattaable-screen.png)

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-dashboard-dattaable.git
$ cd django-dashboard-dattaable
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port 
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and **create a new user**. After authentication, the app will unlock the private pages.

<br />

## Deployment

### [Docker](https://www.docker.com/) execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/athmanziri/changemaker.git
$ cd changemaker
```

> Start the app in Docker

> Development Environment

```bash
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate --noinput
$ docker-compose exec web python manage.py flush --no-input
$ docker-compose exec web python manage.py migrate
$ docker-compose down -v
```


> Production Environment

```bash
$ docker-compose -f docker-compose.prod.yml down -v
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

If the container fails to start, check for errors in the logs via 
```bash
$ docker-compose -f docker-compose.prod.yml logs -f.
```

Again, requests to http://localhost:1337/staticfiles/* will be served from the "staticfiles" directory.

Navigate to http://localhost:1337/admin and ensure the static assets load correctly.

You can also verify in the logs -- via docker-compose -f docker-compose.prod.yml logs -f -- that requests to the static files are served up successfully via Nginx: