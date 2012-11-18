from django.conf.urls import patterns, include, url
from models import *
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'env_admin.views.home', name='home'),
    # url(r'^env_admin/', include('env_admin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url('^$', ResourceListView.as_view(
        #model=Resource,
    )),
)
