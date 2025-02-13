"""
WSGI config for cryptoproject project.

https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
/bwsgi application import DJANGO_SETTINGS_MODULE
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptoproject.settings')

application = get_wsgi_application()
