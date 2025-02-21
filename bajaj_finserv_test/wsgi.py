"""
WSGI config for bajaj_finserv_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bajaj_finserv_test.settings')

application = get_wsgi_application()

# import os
# from django.core.wsgi import get_wsgi_application

# # Set the default settings module for Django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

# application = get_wsgi_application()

