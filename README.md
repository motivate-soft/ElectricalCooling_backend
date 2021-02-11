# Heat Transfer Backend

## Technologies

```
Django/Django Rest Framework
```

## Running project
### create .env file on root dir
```
SECRET_KEY=DJANGO_APP_SECRET_KEY
DB_HOST=DATABASE_HOSTNAME
DB_NAME=DATABASE_NAME
DB_USER=DATABASE_USERNAME
DB_PASSWORD=USER_PASSWORD
```

### virtualenv, dependencies, migrate
You have to install python 3.8+ to run this app
+ Unix, MacOS
```
$ python3 -m venv venv
$ source djangox/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
(venv) $ python manage.py runserver
```
+ Windows
```
$ python3 -m venv venv
$ cd venv/Scripts/activate
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
(venv) $ python manage.py runserver
```

Server listens on [localhost:8000](http://localhost:8000)
