import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SECRET_KEY = '^=2kbsqw#&3$(=1!khq_xf7g3k3el9ygv=z+oiuc=f#s=hx%r_'

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'south',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'sample',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pyowa.urls'

WSGI_APPLICATION = 'pyowa.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
LOCALE_PATHS = (
    BASE_DIR + "/sample/locale",
)
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'
