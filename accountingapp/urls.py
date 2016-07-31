from django.conf.urls import patterns, include, url
from accountingapp.views import *
 
urlpatterns = patterns('',
	url(r'^$', home, name='home'),
    # url(r'^/', home, name="home")
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
   	url(r'^register/$', register_page),
)