from .base import *


DEBUG = False

ADMINS = (('Xor0x', 'xor0x@mail.com'),)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '*****',
    }
}