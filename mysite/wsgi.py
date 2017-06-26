"""
WSGI config for 'mysite' project.

It exposes the WSGI callable as a module-level variable named `application`.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from caduceus.wsgi import Caduceus
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

caduceus_project_id = "a555365e-6b1e-4479-81af-3376c762ceb0"
application = Caduceus(get_wsgi_application(), caduceus_project_id)
        
