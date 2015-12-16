from django.conf.urls import patterns, include, url
from details import views
from details.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Details.as_view(), name='details'),
    url(r'^shows/(?P<id>\w+)/$', Shows.as_view(),name='shows'),
    url(r'^deletes/(?P<id>\w+)/$', Deletes.as_view(),name='Deletes'),
    url(r'^adds/$', Adds.as_view(),name='adds'),
    url(r'^errors/$', Errors.as_view(),name='errors'),
)
