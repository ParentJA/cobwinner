from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin


admin.autodiscover()

# Admin...
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# Prize...
urlpatterns += patterns('',
    url(r'^', include('prize.urls')),
)