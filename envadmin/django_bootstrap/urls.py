from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', hello),
)


