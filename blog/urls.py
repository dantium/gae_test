"""
URLs for blog app.
"""

from django.conf.urls.defaults import *


urlpatterns = patterns('blog.views',
    url(r'^$', 'list_posts', name='blog-listposts'),
    url(r'^post/(?P<slug>[-\w]+)/$', 'display_post', name='blog-displaypost'),
    
    url(r'^create_post/$', 'create_edit_post', name='blog-addpost'),
    url(r'^edit_post/(?P<object_id>\d+)/$', 'create_edit_post', name='blog-editpost'),
    url(r'^delete_post/(?P<object_id>\d+)/$', 'delete_post', name='blog-deletepost'),
)