from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&^hwp6zm63-i%8li+r$_wst)(%*t5z3g4wph*+63qemhk16l30'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
