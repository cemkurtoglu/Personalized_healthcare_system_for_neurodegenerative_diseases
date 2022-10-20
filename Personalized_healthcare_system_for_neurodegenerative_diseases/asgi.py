"""
ASGI config for Personalized_healthcare_system_for_neurodegenerative_diseases project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Personalized_healthcare_system_for_neurodegenerative_diseases.settings')

application = get_asgi_application()
