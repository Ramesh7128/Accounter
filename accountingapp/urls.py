from django.conf.urls import include, url
from accountingapp.views import *
from django.contrib.auth.views import login
 
urlpatterns = [
	url(r'^$', home, name='home'),
    # url(r'^/', home, name="home")
    url(r'^login/$', login),
    url(r'^logout/$', logout_page, name='logout_page'),
   	url(r'^register/$', register_page, name='register_page'),
    url(r'^reports/$', Reports.as_view(), name='reports'),
   	url(r'^clients/$', Clients.as_view(), name='client'),
   	url(r'^addclient/$', AddClient.as_view(), name='addClient'),
   	url(r'^clients/(?P<pk>\d+)/projects/$', Projects.as_view(), name='projects'),
   	url(r'^addproject/(?P<pk>\d+)/$', AddProject.as_view(), name='addProject'),
   	url(r'^project/timelist/(?P<pk>\d+)/$', ProjectTimeList.as_view(), name='ProjectTimeList'),
   	url(r'^addtime/(?P<pk>\d+)/$', AddProjectTime.as_view(), name='AddProjectTime'),



]