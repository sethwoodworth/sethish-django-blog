import os
import sys

sys.path.append('/var/www/sethish.com/')
sys.path.append('/var/www/sethish.com')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler() 
