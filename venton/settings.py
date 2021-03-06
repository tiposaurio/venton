# _*_ coding: utf-8 _*_
"""
Django settings for backengo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qzl9b4r*o&4z1$3*v1wc73^ceg0)7&uvz0vrkpqh%c!_w_mc5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG  # original TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*', ]  # original ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # added
    'django.contrib.sites',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.flatpages',

    # third-party tools
    #'south', en la 1.7 ya no, ahora es django_migrations
    'crispy_forms',

    # mis tools
    'apps.utils',

    # mis apps
    'apps.params',
    'apps.space',
    'apps.sad',
    
    'apps.home',
    'apps.mod_backend',
    'apps.accounts',

)

AUTH_USER_MODEL = 'sad.User' # added
#AUTH_PROFILE_MODULE = "backend.User" # added
SITE_ID = 1 # added

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # added
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'venton.urls'

WSGI_APPLICATION = 'venton.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# added
DATABASESo = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',  # sqlite3
        'NAME': 'xe',
        'USER': 'seral',
        'PASSWORD': 'ccieupeu',
        #'TEST_TBLSPACE': 'seral_default',
        #'HOST': '127.0.0.1',
        #'PORT': '1521',
        #'TEST_USER': 'seral',
        #'TEST_TBLSPACE': 'seral',
        #'TEST_TBLSPACE_TMP': 'django_test_default_temp',
    }
}

DATABASESm = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # sqlite3
        'NAME': 'db2',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
# DESC
DESC = 'DESC'
if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
    DESC = 'ASC'

# end added


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC' # 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# added
from django.utils.translation import ugettext_lazy as _
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
LANGUAGES = (
    ('ja', _('Japanese')),
    ('zh-tw', _('Traditional Chinese')),
    ('fr', _('French')),
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('es-ar', _('Argentinian Spanish')),
    ('es-pe', _('Spanish')),
    ('pt', _('Portuguese')),
    ('pt-br', _('Brazilian Portuguese')),

)
# end added


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# added all
# Absolute path to the directory static files should be collected to.
if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, '/static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
    # para cargar los js y css y tambien para {% load staticfiles %}
    #'./static/',
)
# end static

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION

# render to templates o solo para base.html general
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

# 'str' object has no attribute 'session' para la sessiones de
# messages.get_messages(request)
# TEMPLATE CONFIGURATION #para session.get('flash_msg', False)
# See:
# https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    # 'django.core.context_processors.l10n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)


# Django-crispy-forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Num rows per page
PER_PAGE = 6

import datetime

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)s] [%(path)s] [%(ip)s] [%(user)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose_dj': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {

        'file_django': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'temp/logs',
                                     'dj%s.txt' % (datetime.datetime.now().strftime("%Y-%m-%d"))),
            'formatter': 'verbose_dj'
        },
        'file_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'temp/logs',
                                     'log%s.txt' % (datetime.datetime.now().strftime("%Y-%m-%d"))),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['file_django'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'apps': {
            'handlers': ['file_log'],
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console', ],
        'level': 'INFO'
    },
}



#add email settings, en Sites add registro (obj) localhost:8000
#nota para usuarios activos
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'asullom@gmail.com' #cambie por el suyo
EMAIL_HOST_PASSWORD = '1234567x' #cambie por el suyo
DEFAULT_FROM_EMAIL = 'asullom@gmail.com' #cambie por el suyo

#Backup/restore database https://code.djangoproject.com/wiki/Fixtures
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches  https://pythonhosted.org/johnny-cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        # 'LOCATION': '127.0.0.1:11211',
        #'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    }
}
########## END CACHE CONFIGURATION

########## EXPIRE SESSION BROWSER CLOSE
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True # es manejado por el usuario
########## END EXPIRE SESSION

