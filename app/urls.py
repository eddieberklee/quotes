from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    url(r'^add_quote/$', 'app.views.add_quote', name='add_quote'),
    url(r'^delete_quote/$', 'app.views.delete_quote', name='delete_quote'),
    url(r'^edit_quote/$', 'app.views.edit_quote', name='edit_quote'),
)
