from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from books.views import PublisherList

urlpatterns = patterns('books.views',
                       url(r'^hello/$', 'hello'),
                       url(r'^escape/$', 'escape'),
                       url(r'^meta/$', 'display_meta'),
                       url(r'^search_form/$', 'search_form'),
                       url(r'^search/$', 'search'),
                       url(r'^contact/$', 'contact'),
                       url(r'^contact/thanks/$', 'contact'),
                       url(r'^about/$', TemplateView.as_view(template_name='books/about.html')),
                       url(r'^publishers/$', PublisherList.as_view(template_name='books/publishers.html')),
                       )