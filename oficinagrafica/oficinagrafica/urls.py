from django.conf.urls import patterns, include, url
from django.contrib import admin

from porfolio import views

urlpatterns = patterns('',
    url(r'^porfolio/', include('porfolio.urls', namespace="porfolio")),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'oficinagrafica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
)
