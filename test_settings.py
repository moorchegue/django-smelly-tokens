SECRET_KEY = 'la-la-la'

INSTALLED_APPS = [
    'smelly_tokens',
]

MIDDLEWARE = []

ROOT_URLCONF = 'smelly_tokens.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

SMELLY_TOKENS_APPLICATIONS = [
    'smelly_tokens',
]
