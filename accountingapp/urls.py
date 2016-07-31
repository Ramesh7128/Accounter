from django.conf.urls import include, url
from accountingapp.views import *
from django.contrib.auth.views import login
 
urlpatterns = [
	url(r'^$', home, name='home'),
    # url(r'^/', home, name="home")
    url(r'^login/$', login),
    url(r'^logout/$', logout_page, name='logout_page'),
   	url(r'^register/$', register_page, name='register_page'),
   	url(r'^clients/$', Clients.as_view(), name='client'),
   	url(r'^addclient/$', AddClient.as_view(), name='addClient'),
]