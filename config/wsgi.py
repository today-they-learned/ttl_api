"""
WSGI config for ttl_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from nplusone.ext.wsgi import NPlusOneMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = NPlusOneMiddleware(get_wsgi_application())
