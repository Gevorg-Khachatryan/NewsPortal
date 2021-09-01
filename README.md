# NewsPortal sample application
The project presents itself as the main back-end of news site.
There is no SECRET_KEY in the project.
## Requirements
- Python 3+
- Django 2+

## External libraries

- CKEditor 5 
- Jquery 
- Bootstrap  

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Gevorg-Khachatryan/NewsPortal.git
$ cd NewsPortal
```

Create a virtual environment to install dependencies in and activate it:
```sh
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```
More:
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/


Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Migrate:

```sh
(venv)$ cd project
(venv)$ python manage.py migrate
```
   

Make admin user:

```sh
(venv)$ python manage.py createsuperuser
```
Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
