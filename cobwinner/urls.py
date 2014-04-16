from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin


admin.autodiscover()

# Admin...
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# Main...
urlpatterns += patterns('cobwinner.views',
    url(r'^(?P<code>\w{2}\d{2}\w)$', 'landing', name='landing'),
    url(r'^prizes$', 'prizes', name='prizes'),
)