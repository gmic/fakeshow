from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = ['.fakeshow.nl']
WWW_HOST = "www.fakeshow.nl"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'fakeshow'),
        'USER': os.getenv('DATABASE_USER', 'fakeshow'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'fakeshow'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}