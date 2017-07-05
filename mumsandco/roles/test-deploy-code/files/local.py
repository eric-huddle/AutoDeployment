# Example local settings file

# Leave in debug until sure this is instance running correctly
DEBUG = True
DEBUG_ALIAS = 'release'

# Identify transactions in Braintree as coming from this instance
BRAINTREE_PREFIX = 'rel'

BASE_URL = 'test.huddle.com.au'

DUCKCREEK_STORE_XML = {
    'RSP': True,
    'ZIP': False,
    'REQ': True,
}

SERVICES = {
    'motorweb': True,
    'car_quote': True,
    'travel_quote': True,
}

# Nginx domains that are allowed to run the site itself
ALLOWED_HOSTS = [
    'localhost:3000',
    'localhost:8002',
    '*',
]

# Nginx domains will be allowed to make API calls
CORS_ORIGIN_WHITELIST = [
    'localhost:3000',
    'localhost:8002',
    '*',
]

# Redfine the urls which will be sent to the Angular app
FRONTEND_URL = "http://%s" % BASE_URL
API_URL = "http://api.%s" % BASE_URL
ADMIN_URL = "http://admin.%s" % BASE_URL
#FRONTEND_URL = "http://localhost:3000"
#API_URL = "http://localhost:8000"
#ADMIN_URL = "http://localhost:8001"

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

DUCKCREEK_MODE = 'sandbox'
BRAINTREE_MODE = 'sandbox'
VEDA_MODE = 'sandbox'
SLACK_MODE = 'sandbox'
