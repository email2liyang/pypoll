from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$', 'polls.views.index'),
                       url(r'^(?P<poll_id>\d+)/$', 'polls.views.detail'),
                       url(r'^(?P<poll_id>\d+)/results/$','polls.views.results'),
                       url(r'^(?P<poll_id>\d+)/vote/$','polls.views.vote'),
                       )