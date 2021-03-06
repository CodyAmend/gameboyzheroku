"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 2.0b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w#c2p$9qpf@+%_f14c9g1%4lm*o0s2ht^*+4mx^77l($)l!1!6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
    'streaming.apps.StreamingConfig',
    'social_django',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django_comments',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd2b8o2nvpo6ro1',
        'USER': 'hlqokivhazrsiw',
        'PASSWORD': 'cc3c4297beac61c6ca9d3f0310d8926cb886d0c6d61989ad0e97ed508ec7c275',
        'HOST': 'ec2-54-235-156-60.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}



# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
DATABASES['default'] = dj_database_url.config()

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CART_SESSION_ID = 'cart'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'pythonrocks225@gmail.com'
EMAIL_HOST_PASSWORD = 'eb708199'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


#Braintree settings
BRAINTREE_MERCHANT_ID = 'qdkbfd3csc98nsgb'
BRAINTREE_PUBLIC_KEY = 'zck9qjfcw783rk5k'
BRAINTREE_PRIVATE_KEY = 'b2d2db6c64c891bf7c773911293b1b79'

from braintree import Configuration, Environment

Configuration.configure(
    Environment.Sandbox,
    # Environment.Production,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'shop.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

]

# social auth settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '298571437536-kjq7hq996nih7kptnqiknov3g6vieaik.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '-5HOWZ94RuYoOMlPnxKHp0QV' # Google Consumer Secret

# social auth settings
SOCIAL_AUTH_FACEBOOK_KEY = '2203867496502561' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '518ca15a5c906f95de54257457012f21' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']



STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


