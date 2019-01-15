"""
Django settings for edpm project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .s_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor'
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DKEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#SERVER HOST
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'issuances.apps.IssuancesConfig',
    'vimage.apps.VimageConfig',
    'algoliasearch_django',
    'adminsortable'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'edpm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'edpm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


# CKEditor Config
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'width': 1000,
        'height': 150,
        'toolbar': 'EDPM',
        'toolbar_EDPM': [
            ['Format', 'Styles', 'Bold', 'Italic', 'Underline'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['Table','NumberedList','BulletedList','Link','Unlink'],
            ['RemoveFormat','Source'],
        ],
        'contentsCss': ['/static/ckeditor/ckeditor/contents.css'],
        'stylesSet': [
            {
                'name': 'Note Box' , 
                'element': 'div', 
                'styles': {
                    'padding': '5px 10px', 
                    'background': '#E4E3E2', 
                    'border': '1px solid #ccc', 
                    'width': '66%',
                    'font-style': 'italic',
                    'font-size': '12px'
                    }
            }
        ],        
    }
}

# CKEDITOR.config.extraPlugins:

# vImage config
VIMAGE = {
    'issuances.models': {
        'DIMENSIONS': (1920, 300),
        'SIZE': {'lt': 1000},
    }
}

ALGOLIA = {
    'APPLICATION_ID': AID,
    'API_KEY': AKEY
}

CSRF_COOKIE_HTTPONLY = False

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240