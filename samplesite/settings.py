"""
Django settings for samplesite project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from tempfile import template

import rest_framework.authentication
from django.contrib.messages.context_processors import messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kdsyh9j&6ks^*@$qdpeaqid090k%f6bm16k5w+j+qldjdgvc*q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'captcha',
    # 'django.contrib.postgres',
    'precise_bbcode',
    'django_bootstrap5',
    'easy_thumbnails',
    'rest_framework',
    'corsheaders',

    'bboard.apps.BboardConfig',
    'testapp',

    'django_cleanup', # писать только внизу
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'bboard.middlewares.test_middleware'
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'bboard.middlewares.RubricMiddleware'
]

ROOT_URLCONF = 'samplesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            # 'libralies':{
            #     'bbtags': 'bboard.templatetags.bbtags', # load нужен
            # },
            # 'builtins': [
            #     'bboard.templatetags.bbtags' # load не нужен
            # ],
            # 'autoescape': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.static',
                'bboard.middlewares.rubrics',
            ],
        },
    },
]

WSGI_APPLICATION = 'samplesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'ATOMIC_REQUEST': False,  # по умолчанию
        # 'ATOMIC_REQUEST': True,
        # 'AUTOCOMMIT': True,  # по умолчанию
        # 'AUTOCOMMIT': False,
    }
}

#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "django_db",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# STATIC_ROOT = '/static/'

MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ABSOLUTE_URL_OVERRIDES = {
#     'bboard.rubric': lambda rec: f"/{rec.pk}/"
# }


# LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "bboard:index"
LOGOUT_REDIRECT_URL = "bboard:index"


CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.word_challenge'
# CAPTCHA_LENGTH = 6
CAPTCHA_WORDS_DICTIONARY = os.path.join(BASE_DIR, 'static', 'words.txt')
# CAPTCHA_FONT_SIZE = 22
# CAPTCHA_LETTER_ROTATION = (-35, 35)
CAPTCHA_BACKGROUND_COLOR = '#001100'
CAPTCHA_FOREGROUND_COLOR = '#ffffff'
# CAPTCHA_IMAGE_SIZE = (150, 35)

# DATA_UPLOAD_MAX_MEMORY_SIZE = 2_621_440  # 2.5 Mb

BBCODE_NEWLINE = '<br>'
BBCODE_ESCAPE_HTML = (
    ('&', '&amp;'),
    ('<', '&lt;'),
    ('>', '&gt;'),
    ('"', '&quot;'),
    ('\'', '&#39;'),
)
BBCODE_ALLOW_CUSTOM_TAGS = False
SMILIES_UPLOAD_TO = 'precise_bbcode/smilies'
#
# BOOTSTRAP5= {
#     'required_css_class': 'required',
#     'success_css_class': 'has-success',
#     'error_css_class': 'has-error',
# }

THUMBNAIL_ALIASES = {
    'bboard.Bb.img': {
        'default': {
            'size': (500, 300),
            'crop': 'scale',
        },
    },
    'testapp': {
        'default': {
            'size': (400, 300),
            'crop': 'smart',
            'bw': True
        },
    },
    '': {
        'default':{
            'size': (180, 240),
            'crop': 'scale',
        },
        'big': {
            'size': (480, 640),
            'crop': '10,10',
        },
    },
}

THUMBNAIL_DEFAULT_OPTIONS = {
    'quality': 90,
    'subsampling': 1,

}

# # SESSIONS
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# SESSION_SERIALIZER= 'django.contrib.sessions.backends.'

# # MESSAGES
# MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
# MESSAGE_LEVEL = 20 # INFO
# MESSAGE_LEVEL = messages.DEBUG

# # EMAILS
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend" # django.core.main.outbox
# EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

# DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# Только с SMTP
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = False
EMAIL_USE_TSL = False

EMAIL_SSL_CESTFILE = None
EMAIL_SSL_KEYFILE = None

EMAIL_TIMEOUT = None
EMAIL_USE_LOCALTIME = False

# Только для "django.contrib.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = ''

ADMINS = [
    ('admin', 'admin@localhost'),
]

MANAGERS = [
    ('manager', 'manager@localhost'),
]


# # CORS HEADERS
CORS_ALLOW_ALL_ORIGINS = True
CORS_URLS_REGEX = r'/api/.*$'
#
# CORS_ALLOW_ORIGINS = [
#     'http://www.bboard.ru'
# 'http://www.bboard.ru'
# 'http://www.bboard.ru'
# 'http://www.bboard.ru'
# ]
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r'^https?://(www|admin)\.bboard\.ru$',
#     r'^http://(www\.)\?bb\.net$',
# ]
# CORS_ALLOW_METHOD = ['GET','POST']

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        # 'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.DjangoModelPermissions',
        # 'rest_framework.permissions.DjangoModelPermissionOrAnonReadOnly'
    ),
    'DEFAULT_AUTHENTICATED_CLASES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
# from django.contrib.auth import get_user_model
# user = get_user_model().objects.get(is_superuser=True)
# user.set_password('qwerty123')
# user.save()
