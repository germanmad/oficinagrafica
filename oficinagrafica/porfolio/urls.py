from django.conf.urls import patterns, url

from porfolio import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<work_id>\d+)/$', views.detail, name='detail'),
   
)