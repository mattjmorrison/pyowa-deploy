from django.conf.urls import patterns, url
from sample.views.person import Person, People


urlpatterns = patterns(
    '',
    url(r'^people/$', People.as_view(), name='people'),
    url(r'^people/(?P<pk>\d)/$', Person.as_view(), name='person'),
)
