"""
ASGI config for Django_eCommerce project.

It exposes the ASGI callable as a module-level variable named ``application``. # replace with pet app's name

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_eCommerce.settings')

application = get_asgi_application()