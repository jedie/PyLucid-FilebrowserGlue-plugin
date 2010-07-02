# coding: utf-8

from django.conf.urls.defaults import patterns, url, include

from filebrowser_glue.views import url_info

urlpatterns = patterns('',
    url(r'', include('filebrowser.urls')),
    url(r'^', url_info, name="filebrowser-glue-url_info"),
)
