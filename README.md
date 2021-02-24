

# The Interview Manager



## Summary
### A team of evaluators can enjoy the Interview Manager organizing the interview meeting and keep track of candidates' history.

### Using the service, evaluators can create an account, add candidates, take some notes for each one or delete any of them. The evaluators can also enjoy search, filter, sort, and paginations.

## Tools

- Python 3.7
- Django 3.1

## 3rd party

- django-filter==2.4.0
- psycopg2-binary==2.8.4
- django_tables2
- django-bootstrap3


## Local Installation


### Setup virtualenv
- pipenv --python 3.7
- pipenv shell

### Dependencies
- sudo apt-get install postgresql postgresql-contrib
- pipenv install -r requirements.txt

### Initialize database
- sudo -u postgres psql
- CREATE DATABASE name;
- CREATE USER user WITH PASSWORD 'pass';
- ALTER ROLE user SET client_encoding TO 'utf8';
- ALTER ROLE user SET default_transaction_isolation TO 'read committed';
- ALTER ROLE user SET timezone TO 'Asia/Tehran';
- GRANT ALL PRIVILEGES ON DATABASE name TO user;
- \q
- exit

### Configure database in django settings
- 'ENGINE': 'django.db.backends.postgresql',
- 'NAME': 'name',
- 'USER': 'user',
- 'PASSWORD': 'pass',
- 'HOST': '127.0.0.1',
- 'PORT': '5432',

### Run
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver






