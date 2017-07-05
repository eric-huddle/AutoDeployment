from base import *
from datetime import timedelta

ROOT_URLCONF = 'urls.api'

APP_NAME = 'API'

MIDDLEWARE_CLASSES += [
    'corsheaders.middleware.CorsMiddleware',
    'core.middleware.MaintenanceMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'users.auth.QuerystringJSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.AllowAny',
    ),
    # 'EXCEPTION_HANDLER': 'common.server_errors.graceful_exception_handler',
}

if not DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
    )

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': timedelta(minutes=JWT_AUTHENTICATION['TIMEOUT_MINUTES']),
    'JWT_ALLOW_REFRESH': True,
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.auth.jwt_response_payload_handler',
}

CORS_ORIGIN_WHITELIST = CORS_ORIGIN_WHITELIST + [
    BASE_URL,
    'staging.%s' % BASE_URL,
    'we-are-updating.%s' % BASE_URL,
]

