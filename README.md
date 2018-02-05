```
computer$ mkvirtualenv cobwinner
(cobwinner) computer$ pip install -r requirements/local.txt
(cobwinner) computer$ createuser -d -e -s -W cobwinner
Password: pAssw0rd!
CREATE ROLE cobwinner SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;
(cobwinner) computer$ createdb -e -O "cobwinner" cobwinner
CREATE DATABASE cobwinner OWNER cobwinner;
(cobwinner) computer$ export DB_NAME=cobwinner
(cobwinner) computer$ export DB_USER=cobwinner
(cobwinner) computer$ export DB_PASS=pAssw0rd!
(cobwinner) computer$ python manage.py makemigrations prize
(cobwinner) computer$ python manage.py migrate
(cobwinner) computer$ python manage.py createsuperuser
Username (leave blank to use 'computer'): admin
Email address: admin@example.com
Password: pAssw0rd!
Password (again): pAssw0rd!
Superuser created successfully.
(cobwinner) computer$ python manage.py loaddata ./prize/fixtures/prizes.json
Installed 3625 object(s) from 1 fixture(s)
```