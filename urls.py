from django.conf.urls.defaults import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('djblog.ishblog.urls')),
    url(r'^$', 'djblog.ishblog.views.static'),

    #url(r'^projects/', include('djblog.projects.urls')),
    #url(r'^rss/', include('djblog.rss.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
