import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # I don't think this is ever used
    ('Seth Woodworth', 'seth+sethblog@sethish.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Just using a local temp sql site
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'temp.sql',
    }
}

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = True

# Base director.
BASE_DIR = os.path.dirname(__file__)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Local folder containing media and static files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = 'media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, './static/'),
)

# List of finder classes that know how to find static files in  various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0gdekfmxl+(#bpo2@r(#wtllod8qi9k^$m+t%x@#!(om8rapl&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    # this enables per-app temploate loading: `$project/$app/templates/*`
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'djblog.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'djblog.ishblog',
)

# A sample logging configuration. 
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
