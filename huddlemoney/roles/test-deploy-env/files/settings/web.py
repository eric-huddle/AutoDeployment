from base import *


ROOT_URLCONF = 'urls.web'

APP_NAME = 'WEB'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(BASE_DIR, 'backend/templates'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'users.context.urls',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    # 'reversion.middleware.RevisionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middleware.MaintenanceMiddleware',
)


if DEBUG or FRONTEND_URL.find('localhost') > -1:

    # when we run localhost:8002

    STATICFILES_DIRS = [
        ('scripts', path.join(BASE_DIR, 'build/dist/static/scripts')),
        ('styles', path.join(BASE_DIR, 'build/dist/static/styles')),
        ('favicons', path.join(BASE_DIR, 'build/dist/assets/favicons')),
        ('assets', path.join(BASE_DIR, 'build/dist/assets')),
    ]
