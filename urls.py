from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('djblog.ishblog.urls')),

    #url(r'^projects/', include('djblog.projects.urls')),
    #url(r'^rss/', include('djblog.rss.urls')),
)
