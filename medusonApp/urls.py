from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',

	(r'^$','medusonApp.views.index'),
	(r'clients/$','medusonApp.views.clients'),
	(r'clients/nouveau/$','medusonApp.views.addClient'),
	(r'clients/(?P<client_id>\d+)$','medusonApp.views.clientDetail'),
)
