from django.conf.urls.defaults import *

urlpatterns = patterns('ishblog.views',
    url(r'^$',                              'list',      name='blog-list-newest'),
    url(r'^page/(\d+)/$',                   'list',      name='blog-list-page'),
    url(r'^0(\d+)/(.*)/$',                   'entry',     name='blog-entry'),

    # borrowed from Stevelosh, kept here for reference
    # TODO: Clean/integrate/delete these extra URL lines
    #url(r'^(\d+)/(\d+)/(\d+)/(.*).html/$',  'old_entry', name='blog-old-entry'),
    #url(r'^comment/$',                      'comment',   name='blog-post-comment'),
)
