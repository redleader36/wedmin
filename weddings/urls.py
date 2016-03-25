from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /weddings/
    url(r'^$', views.index, name='index'),
    # ex: /weddings/5/
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /weddings/5/guests/
    url(r'^(?P<event_id>[0-9]+)/guests/$', views.list, name='list'),
    # ex: /weddings/5/vote/
    url(r'^guest/(?P<guest_id>[0-9]+)/$', views.info, name='info'),
]