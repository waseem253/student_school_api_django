# School Student API Django

## Python Version: Python 3.8

## Setup

The first thing to do is to clone the repository:

```sh
git@github.com:waseem253/student_school_api_django.git
cd student_school_api_django
```

Create a virtual environment to install the dependencies and activate it:

```sh
python -m venv venv
```
Activate virtual environment
```
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

Then install the dependencies:

```sh
(venv) pip install -r requirements.txt
```
or if you want to install with pipenv 
```sh
(venv) pipenv install
```
Note that pipenv will also create a virtual enviorment so you can activate that as well

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

## Configurations
Go to the 
```sh
(venv) cd manatal/
```
Open the `settings.py` file:
find the to the DATABASE settings/section and replace the `NAME` `USER` and `PASSWORD` with your own credentials 
## Migration
move one step back to the directory
```sh
(venv) cd ..
```
type the following command
```sh
(venv) python3 manage.py migrate
```
you shall see all the migrations runing

## Run application

To run the application, stay in the same directory where `manage.py` is
```sh
(venv) python manage.py runserver
```
## Routes
**To see the routes and the payload i have attached a postman collection**
