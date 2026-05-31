from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-smartinventory'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'inventory',

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

ROOT_URLCONF = 'smartinventory.urls'

TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [

            BASE_DIR / 'inventory/templates'

        ],

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

WSGI_APPLICATION = 'smartinventory.wsgi.application'

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'id-id'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [

    BASE_DIR / 'inventory/static'

]
JAZZMIN_SETTINGS = {
    "site_title": "SmartInventory Admin",
    "site_header": "SmartInventory Campus",
    "site_brand": "SmartInventory",
    "welcome_sign": "Welcome to SmartInventory Campus System",
    "copyright": "Maulizar",
    
    "site_logo_classes": "img-circle",

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "inventory.Barang": "fas fa-box",
        "inventory.Kategori": "fas fa-tags",
    },

    "custom_css": "css/admin.css",
}

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/dashboard/'

LOGOUT_REDIRECT_URL = '/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

JAZZMIN_SETTINGS = {

    "site_title": "SmartInventory Admin",

    "site_header": "SmartInventory Campus",

    "site_brand": "SmartInventory",

    "welcome_sign": "Welcome to SmartInventory Campus System",

    "copyright": "Maulizar",

    "site_logo_classes": "img-circle",

    "show_sidebar": True,

    "navigation_expanded": True,

    "icons": {

        "auth": "fas fa-users-cog",

        "auth.user": "fas fa-user",

        "inventory.Barang": "fas fa-boxes",

        "inventory.Kategori": "fas fa-tags",
    },

    "custom_css": "css/admin.css",
}