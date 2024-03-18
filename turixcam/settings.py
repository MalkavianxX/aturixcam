"""
Django settings for turixcam project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7@-@+wzqd+*@34%3)6=%*p(er_c(sn$arx+e%pj$jzr*fkfrye'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# settings.py

if not DEBUG:
    SECURE_SSL_REDIRECT = True

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'camaras',
    'evento',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_bunny',
    'equipo',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",

]

ROOT_URLCONF = 'turixcam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'turixcam.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


CSRF_TRUSTED_ORIGINS = ['https://turixcam.com','https://androidturixcam-5zx6p.ondigitalocean.app/','https://king-prawn-app-smyqm.ondigitalocean.app/']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'turixcliente',
        'USER': 'root',
        'PASSWORD': 'Rmpv54321',
        'HOST': 'postgresql-156478-0.cloudclusters.net',  # Puedes cambiar esto según tu configuración de PostgreSQL
        'PORT': '19998',       # Puerto predeterminado de PostgreSQL
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/


LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
 
STATIC_URL = 'static/'
STATIC_ROOT =  os.path.join(BASE_DIR,'static') 
MEDIA_URL= '/media/'
MEDIA_ROOT =  os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'login.CustomUser'

#cliente id: 553853177313-1ibj1o1vm885hgosr8pummk8bnhpol9k.apps.googleusercontent.com
#secreet key: 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
LOGIN_REDIRECT_URL = "/profile"
LOGUT_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = 'render_init_page'
LOGIN_URL = 'view_user_login'
 
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_ADAPTER = 'login.myadapter.MyAccountAdapter'
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}


# Estas se pueden encontrar en el panel de control de tu almacenamiento en `FTP & API Access`
BUNNY_USERNAME = "turixstatic"
BUNNY_PASSWORD = "cb58e653-373f-432f-9cd02f0643ee-cf5a-43ff"
# Este es el código de la región de almacenamiento. Por ejemplo, Los Ángeles es `la`, Singapur es `sg`, etc. El valor predeterminado es `ny` (Nueva York).
BUNNY_REGION = "la"
# Opcional. Por ejemplo, `https://myzone.b-cdn.net/`. Se utilizará `MEDIA_URL` si no se establece esto.
BUNNY_HOSTNAME = "https://staticurix.b-cdn.net/"
# Opcional. Por ejemplo, `static/`. Si no se establece, los archivos se almacenarán en el directorio raíz del almacenamiento.
BUNNY_BASE_DIR = "static/"


EMAIL_HOST = 'smtpout.secureserver.net'  # El host de tu servidor de correo
EMAIL_PORT = 587  # El puerto que usa tu servidor de correo
EMAIL_HOST_USER = 'soporte@turixcam.com'  # Tu dirección de correo
EMAIL_HOST_PASSWORD = 'turixcam2023'  # La contraseña de tu correo
EMAIL_USE_TLS = True  # Si tu servidor de correo usa TLS
