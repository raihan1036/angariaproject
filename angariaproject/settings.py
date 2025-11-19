"""
Django settings for angariaproject project.
"""

# settings.py

import os  # <-- This is correct
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4g*soxl4l#1o_@6o6q!1=z!0ct11l3wortqoza(8mmfx8m&o3!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True







# angariaproject/settings.py

# Allow anyone to access (Only for this 1-week test!)
ALLOWED_HOSTS = ['*'] 
# অথবা সিকিউরিটির জন্য নির্দিষ্ট ডোমেইন দিন: ['.ngrok-free.app', '127.0.0.1', 'localhost']



CSRF_TRUSTED_ORIGINS = [
    'https://*.ngrok-free.dev',
    'https://*.ngrok-free.app', 
    'https://cruciately-transfrontal-marry.ngrok-free.dev'
]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Custom Apps
    'core',
    'news',
    'metrics',
    'Login',
    
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

ROOT_URLCONF = 'angariaproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'templates' ফোল্ডারটি এখানে যোগ করা হলো
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'angariaproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i1n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Static Files: আপনার CSS/JS ফাইলগুলোর জন্য (This is correct)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media Files: ব্যবহারকারীর আপলোড করা ছবির জন্য
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Login/Logout Redirects ---
# লগইন করার পর কোথায় যাবে (হোমপেজ)
LOGIN_REDIRECT_URL = '/'
# লগআউট করার পর কোথায় যাবে (হোমপেজ)
LOGOUT_REDIRECT_URL = '/'