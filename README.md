django-poll-app
===============

The solution to https://docs.djangoproject.com/en/dev/intro/tutorial01/

Getting Started
---------------

## Initial Setup

### Base Setup

```
# create a new virtualenv
virtualenv env

# Activate virtualenv
source env/bin/activate

# install Django and Caduceus
pip install Django 
pip install caduceus
```

### Register at Caduceus

1. Login and create a new project
2. Follow instructions and copy the `wsgi` file contents to `mysite/wsgi.py`
3. Run the server `python manage.py runserver`
4. Open the website in the browser at ``http://localhost:8000/polls`` or admin at ``http://localhost:8000/admin`` (admin:admin)
