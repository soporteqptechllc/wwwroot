"""
URL DE APP LOCAL
"""
import os
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','192.170.1.251']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangosap_db',
        'USER': 'adminsapapp',
        'PASSWORD': '#Barraza2022',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
     os.path.join(BASE_DIR, 'static'),
 )
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Otra manera de indicarle la ruta a la carpeta 'static'
#STATICFILES_DIRS = [BASE_DIR.child('static')]

# STATIC_URL = 'static/'