## How to use it

```bash
$ # Get the code
$ git clone https://github.com/swahilipothub/changemaker.git
$ cd changemaker/app
$
$ # Virtualenv modules installation (Unix based systems)
$ python3 -m venv venv
$ source venv/bin/activate
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
$ git clone https://github.com/swahilipothub/changemaker.git
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
$ cp .env.prod.example .env.prod
$ cp .env.prod.db.example .env.prod
$ docker-compose -f docker-compose.prod.yml down -v
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

If the container fails to start, check for errors in the logs via 
```bash
$ docker-compose -f docker-compose.prod.yml logs -f.
```

Again, requests to http://localhost/staticfiles/* will be served from the "staticfiles" directory.

Navigate to http://localhost/admin and ensure the static assets load correctly.

You can also verify in the logs -- via docker-compose -f docker-compose.prod.yml logs -f -- that requests to the static files are served up successfully via Nginx:


Ensure the default Django tables were created:

$ docker-compose exec db psql --username=changemaker --dbname=changemaker_prod
$ \l
$ \c chnagemaker_prod
$ \dt
$ \q