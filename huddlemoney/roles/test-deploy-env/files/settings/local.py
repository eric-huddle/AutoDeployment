# Example local settings file

# Leave in debug until sure this is instance running correctly
DEBUG = True

# Identify transactions in Braintree as coming from this instance
BRAINTREE_PREFIX = 'rel'

# Custom URLs for this instance
BASE_URL = 'test.huddle.com.au'

# Nginx domains that are allowed to run the site itself
ALLOWED_HOSTS = [
    BASE_URL,
    'api.%s' % BASE_URL,
    'admin.%s' % BASE_URL,
    'localhost:3000',
    'localhost:8002',
]

# Nginx domains will be allowed to make API calls
CORS_ORIGIN_WHITELIST = [
    BASE_URL,
    'localhost:3000',
    'localhost:8002',
]

# Redfine the urls which will be sent to the Angular app
FRONTEND_URL = "http://%s" % BASE_URL
API_URL = "http://api.%s" % BASE_URL
ADMIN_URL = "http://admin.%s" % BASE_URL

# Database instance details
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'huddlemoneytestdb',
        'HOST': 'localhost',
        'USER': 'huddlemoney-test-db-user',
        'PASSWORD': 'huddle123',
    }
}

BRAINTREE_MODE = 'sandbox'
VEDA_MODE = 'sandbox'
CUSTOMERIO_MODE = 'sandbox'
DUCKCREEK_MODE = 'sandbox'


LOGGERS = {
   # 'core': {
   #     'handlers': ['debugfile'],
   #     'level': 'DEBUG',
   # },
   # 'quotes': {
   #     'handlers': ['infofile'],
   #     'level': 'INFO',
   # },
   'policies': {
       'handlers': ['debugfile'],
       'level': 'DEBUG',
   },
   'policies': {
       'handlers': ['infofile'],
       'level': 'INFO',
   },
   'payments': {
       'handlers': ['debugfile'],
       'level': 'DEBUG',
   },
   'payments': {
       'handlers': ['infofile'],
       'level': 'INFO',
   },
   # 'points': {
   #     'handlers': ['debugfile'],
   #     'level': 'DEBUG',
   # },
   # 'users': {
   #     'handlers': ['debugfile'],
   #     'level': 'DEBUG',
   # },
   # 'celery': {
   #     'handlers': ['infofile'],
   #     'level': 'INFO',
   # },
}

