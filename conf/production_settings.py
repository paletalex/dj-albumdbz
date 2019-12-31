from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['albumtoon.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'deorugc25mrl1v',
        'USER': 'edbjxhfxcdsrbe',
        'PASSWORD': '3189c301613912168e850409e5851f3467de48810aab3437d75b2d3f6245b9e9',
        'HOST': 'ec2-174-129-33-217.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')