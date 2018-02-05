# Standard library imports.
import os

# Django imports.
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local')

application = get_wsgi_application()
