from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from request.views import *
from subject.views import *
from resource.views import *
from views import *
from rest_framework.urlpatterns import format_suffix_patterns


import resource
import forms
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'env_admin.views.home', name='home'),
    # url(r'^env_admin/', include('env_admin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^$', index),
    #url(r'^projects/$', projects),
    #url(r'^projects/cards/$', project_cards),
    #url(r'^partners/$', partners),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^hello/$', hello),
    (r'^resource/', include('resource.urls')),
    (r'^request/', include('request.urls')),
    #url(r'^login/$', login_view),
    url(r'^login/$', general_form,{'formClass':forms.LoginForm}),
    url(r'^logout/$', logout_view),
    url(r'^API-AUTH/', include('rest_framework.urls', namespace='rest_framework'))

)


# for development only
# This will only work if DEBUG is True.
urlpatterns += staticfiles_urlpatterns()




urlpatterns += patterns('webapp.views',
    url(r'^$', 'api_root'),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^groups/$', GroupList.as_view(), name='group-list'),
    url(r'^groups/(?P<pk>\d+)/$', GroupDetail.as_view(), name='group-detail'),
)

# Format suffixes
#urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
