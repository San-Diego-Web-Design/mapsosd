#! /var/www/mapsosd/wsgi/mapsosd.wsgi
import site, os
site.addsitedir('/var/www/geonode/wsgi/geonode/lib/python2.6/site-packages')
site.addsitedir('/var/www')
site.addsitedir('/var/www/mapsosd')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mapsosd.settings'
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
