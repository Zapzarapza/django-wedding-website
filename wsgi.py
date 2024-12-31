"""
WSGI config for bigday project.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# This path is now set in passenger_wsgi.py:
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigday.settings")

# application variable named 'app' so that there's no confusion
# when passenger_wsgi imports this for its application variable
app = get_wsgi_application()
