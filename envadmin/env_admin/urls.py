from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from devsupport.views import *
from subject.views import *
from resources.views import *
from views import *
import resources
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'env_admin.views.home', name='home'),
    # url(r'^env_admin/', include('env_admin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^$', index),
    url(r'^projects/$', projects),
    url(r'^projects/cards/$', project_cards),
    url(r'^partners/$', partners),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^hello/$', hello),
    (r'^resources/', include('resources.urls')),
)


# for development only
# This will only work if DEBUG is True.
urlpatterns += staticfiles_urlpatterns()
