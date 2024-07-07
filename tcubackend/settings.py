"""
Django settings for tcubackend project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

from core.logging.handlers import WebhookHandler


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY=config('SECRET_KEY')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h3$9j3%^*63(=j-2(@col83qx#qmk%-8f$539dgi=&b&8mptq+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "anymail",
    "corsheaders",
    "drf_spectacular",
    "debug_toolbar",
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'treblle',
]


CUSTOM_APPS = [
    'customauth.apps.UserAppConfig',
    "core",
    "emailer",
    'contactus',
    'socialauth',
    'internship.apps.InternshipAppConfig',
    'load_data'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

AUTH_USER_MODEL = 'customauth.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "core.middleware.RequestIDMiddleware",
    "core.middleware.ExceptionHandlerMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'treblle.middleware.TreblleMiddleware',
]

ROOT_URLCONF = 'tcubackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR/'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tcubackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "core.exception_handlers.custom_exception_handler",
}

# ? Documentation Settings
SPECTACULAR_SETTINGS = {
    "TITLE": "TCU API",
    "DESCRIPTION": "API Documentation for TCU",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
    "DISABLE_ERRORS_AND_WARNINGS": True,
    "SCHEMA_COERCE_PATH_PK_SUFFIX": True,
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:3000',
    'http://localhost:5173',
    'http://localhost:5174',
    'https://tcu-eoxz.vercel.app',
]

CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ['*']

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

TREBLLE_INFO = {
'api_key': config('TREBLLE_API_KEY'),
'project_id': config('TREBLLE_PROJECT_ID')
}

# Google Oauth2 settings
GOOGLE_OAUTH2_CLIENT_ID = config('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = config('GOOGLE_OAUTH2_CLIENT_SECRET')
BASE_FRONTEND_URL = config('BASE_FRONTEND_URL')

CORS_ALLOW_CREDENTIALS = True

from datetime import timedelta

ACTIVATE_JWT = True
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=500),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    }

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.googlemail.com"
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config("DEFAULT_SENDER")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Cloudinary
cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME"),
    api_key=config("CLOUDINARY_API_KEY"),
    api_secret=config("CLOUDINARY_API_SECRET"),
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}

# cloudinary.config(
#   cloud_name = config('CLOUDINARY_CLOUD_NAME'),
#   api_key = config('CLOUDINARY_API_KEY'),
#   api_secret = config('CLOUDINARY_API_SECRET')
# )


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
            "formatter": "verbose",
            "level": config("DJANGO_LOG_LEVEL", "INFO"),
        },
        "webhook": {
            "()": WebhookHandler,
            "formatter": "verbose",
            "webhook_url": config('WEBHOOK_URL'),  # Your webhook URL
            "level": "INFO",  # Send only ERROR and above logs to the webhook
        },
    },
    "loggers": {
        "": {  # The empty string indicates ~ All Apps including installed apps
            "handlers": ["file", "webhook"],  # Add the webhook handler
            "propagate": True,
        },
    },
    "formatters": {
        "verbose": {
            "format": (
                "{asctime} ({levelname}) -  {module} {name} {process:d} {thread:d}"
                " {message}"
            ),
            "style": "{",
        },
        "simple": {
            "format": "{asctime} ({levelname}) -  {message}",
            "style": "{",
        },
    },
}