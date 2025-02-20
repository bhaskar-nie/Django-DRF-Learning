"""
WSGI config for concept_7_p2_modelserialiser_validators project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concept_7_p2_modelserialiser_validators.settings')

application = get_wsgi_application()
