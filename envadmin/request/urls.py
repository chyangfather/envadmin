from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from models import *
from views import *
from rest_framework.generics import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'env_admin.views.home', name='home'),
    # url(r'^env_admin/', include('env_admin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url('^projects$', projects),#ResourceListView.as_view(model=Resource,)),
	url('^request/', request_form_view)
)
