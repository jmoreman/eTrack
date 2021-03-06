from .common import *

SECRET_KEY = "DEVELOPMENT_DO_NOT_USE_IN_PRODUCTION"

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'etrack_development',
        'USER': 'root',
        'HOST': '127.0.0.1',
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
