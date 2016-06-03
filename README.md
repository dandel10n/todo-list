# todo-list
I've desided to become a web programmer and it is my study project. Here you can find how to start the progect.

## How to clone the project

`$ git clone https://github.com/dandel10n/todo-list.git` 

Link could be faund in the repo by clicking the "Clone or download" button

## How to create virtual environment

You should install virtualenv:
`$ sudo pip3 install virtualenv`

then to create venv in necessary dir write:
`$ virtualenv NAMEOFVENV`

next step is to activate venv:
`$ source NAMEOFVENV/bin/activate`

if you need to deactivate venv:
`$ deactivate`

## How to install dependencies

You need to create requirements.txt were the list of dependencies will be kept:
Django==1.9.6
psycopg2==2.6.1

then run `$ pip install -r requirements.txt` to install all the dependencies

## How to setup database (how to create database and how to run migrations)

* First of all you need to install PostgreSQL: `$ sudo apt-get install postgresql postgresql-contrib`
* then `$ sudo -u postgres psql postgres` - authorised as default postgres user
* next we need to create a user: `CREATE USER name WITH PASSWORD 'password';`
* then create database: `CREATE DATABASE name WITH OWNER name;`

to exit write `"\q"`

to run migrations you should write: `$ python manage.py migrate`

## How to run development web server

`$ python manage.py runserver`


