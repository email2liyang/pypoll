from django.conf.urls import patterns, url

urlpatterns = patterns('books.views',
                       url(r'^hello/$', 'hello'),
                       url(r'^escape/$', 'escape'),
                       url(r'^meta/$', 'display_meta'),
                       url(r'^search_form/$', 'search_form'),
                       url(r'^search/$', 'search'),
                       url(r'^contact/$', 'contact'),
                       url(r'^contact/thanks/$', 'contact'),
                       )