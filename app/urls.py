from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    url(r'^add_quote/$', 'app.views.add_quote', name='add_quote'),
)
