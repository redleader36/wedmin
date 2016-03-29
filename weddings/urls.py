from django.conf.urls import url

from . import views

app_name='weddings'
urlpatterns = [
    # # ex: /weddings/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /weddings/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /weddings/5/guests/
    url(r'^(?P<event_id>[0-9]+)/guests/$', views.guestlist, name='guestlist'),
    # ex: /weddings/5/vote/
    url(r'^guest/(?P<guest_id>[0-9]+)/$', views.guestdetail, name='guestdetail'),
]