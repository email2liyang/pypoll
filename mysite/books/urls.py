from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^hello/$', 'books.views.hello'),
                       url(r'^meta/$', 'books.views.display_meta'),
                       url(r'^search_form/$', 'books.views.search_form'),
                       url(r'^search/$', 'books.views.search'),
                       url(r'^contact/$', 'books.views.contact'),
                       url(r'^contact/thanks/$', 'books.views.contact'),
                       )