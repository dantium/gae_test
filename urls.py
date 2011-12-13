from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls') ),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {}, name='auth-login'),
    url(r'^logout/$', 'logout', {'next_page': '/login/'}, name='auth-logout'),  
)