from .base import * 

SECRET_KEY = '-u(rewywy9-hzhcrx1+4=4@e!%0-_0a*x+zo53b14=*2^-mbn_'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}
