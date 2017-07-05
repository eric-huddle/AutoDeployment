"""Account details for Huddlemoney's third party service providers.
"""

# Facebook
FACEBOOK_APP_ID = {
    "sandbox": 1587874741510736,
    "production": 1587874344844109,
}
FACEBOOK_MODE = 'sandbox'

# Braintree
BRAINTREE = {
    'sandbox': [
            'dgvqvyvgt82932n3',
            'k5zr5rbyv2wpwh3g',
            'b277c9c2d4c603d9ea7f43c6f5c391e2',
        ],
    'production': [
            'mrrkk7sss6rysq8r',
            'zvg6m77n48yzcpsh',
            'e91675c1fb309026a05b1cfc63fbee90',
    ],
    'monthly-subscription-plan-id': 'car-monthly',
}

BRAINTREE_MODE = 'sandbox'
BRAINTREE_PREFIX = '' # non-production only

BRAINTREE_TRANSACTION_URL = {
    'sandbox': 'https://sandbox.braintreegateway.com/merchants/%s/transactions/%s',
    'production': 'https://www.braintreegateway.com/merchants/%s/transactions/%s',
}

# Veda
VEDA_SETTINGS = {
    'sandbox': {
        'username': 'HMUMzGCrSc',
        'password': 'RffLKZQsgI',
        'client-ref-prefix': 'HUDMON-TEST-',
        'operator-id': 'HUDMON-TEST',
        'operator-name': 'Huddle Money Live',
        'endpoint': 'https://cteau.vedaxml.com/sys2/soap11/vedascore-apply-v2-0',
    },
    'production': {
        'username': 'HM4gX8392v',
        'password': '7flbeVTQir',
        'client-ref-prefix': 'HUDMON-LIVE-',
        'operator-id': 'HUDMON-LIVE',
        'operator-name': 'Huddle Money Live',
        'endpoint': 'https://vedaxml.com/sys2/soap11/vedascore-apply-v2-0',
    }
}

VEDA_MODE = 'sandbox'

# Addressify
ADDRESSIFY_URL = 'http://api.addressify.com.au/'
ADDRESSIFY_API_KEY = 'ffef0917-57a0-470a-921f-bb6ff62766fc'

# Slack
SLACK_NOTIFICATIONS = True
SLACK_MODE = 'sandbox'

SLACK = {
    'endpoint': 'https://hooks.slack.com/services/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',
    'sandbox': {
        'general-channel': '#huddle-money-test',
        'monitoring-channel': '#huddle-money-test',
    },
    'production': {
        'general-channel': '#huddle-money',
        'monitoring-channel': '#hm-monitoring',
    }
}


MOTORWEB = {
    'sandbox': {
        'URL': 'https://robot.motorweb.com.au/b2b/autoid/generate/xml/1.0',
        'CERT_PATH': 'conf/ssl/motorweb/sandbox/cert.pem',
        'KEY_PATH': 'conf/ssl/motorweb/sandbox/nopass_key.pem',
    },
    'production': {
        'URL': 'https://robot.motorweb.com.au/b2b/autoid/generate/xml/1.0',
        'CERT_PATH': 'conf/ssl/motorweb/prod/cert.pem',
        'KEY_PATH': 'conf/ssl/motorweb/prod/nopass_key.pem',
    },
}

MOTORWEB_MODE = 'sandbox'


# DuckCreek Car Insurance Quote engine
DUCKCREEK = {
    'sandbox': {
        'URL': 'https://dcthbpdev.hollard.com.au/duckcreek/dctserver.aspx',
        'USERNAME': 'admin',
        'PASSWORD': 'admin',
        'USE_SSL': True,
    },
    'production': {
        'URL': 'https://dcthbp.hollard.com.au/duckcreek/dctserver.aspx',
        'USERNAME': 'admin',
        'PASSWORD': 'admin',
        'USE_SSL': True,
    },
}
DUCKCREEK_MODE = 'sandbox'

GOOGLE_RECAPTCHA = {
    'SECRET_KEY': '6LePiCkTAAAAAPHanLn0GrhDMqlyIXi_SfP_IPtJ',
    'ENDPOINT': 'https://www.google.com/recaptcha/api/siteverify',
    'SITE_KEY': '6LePiCkTAAAAALCbQH8fJ6TJ-V3xo3oZiYzf7Fx9',
}

# Google Tag Manager
GOOGLE_TAG_MANAGER_ID = 'GTM-KRQ6V7'

# Zendesk
ZENDESK_ID = 'huddlemoney'

ZENDESK = {
    'URL': 'https://%s.zendesk.com/api/v2' % ZENDESK_ID,
    'USERNAME': 'jonathan@huddlemoney.com.au',
    'PASSWORD': '2trLW6Uqv6N20Y5S4yk9EQzHdK58W5BIYZXMYZXn',
    'DEFAULT_FROM_EMAIL': 'jonathan@huddle.com.au',
    'DEFAULT_FROM_NAME': 'Jonathan Buck',
}

# Inspectlet
INSPECTLET_ID = '1299558559'

# Mandrill
MANDRILL_ENDPOINT = 'https://mandrillapp.com/api/1.0'
