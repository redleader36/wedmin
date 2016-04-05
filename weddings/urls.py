from django.conf.urls import url

from . import views

app_name='weddings'
urlpatterns = [
    # # ex: /weddings/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.EventListView.as_view(), name='event-list'),
    url(r'^new/$', views.EventNewView.as_view(), name='event-new'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.EventDeleteView.as_view(), name='deleteevent'),

    # ex: /weddings/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /weddings/5/guests/
    # url(r'^(?P<event_id>[0-9]+)/guests/$', views.guestlist, name='guestlist'),
    url(r'^(?P<pk>[0-9]+)/guests/$', views.GuestListView.as_view(), name='guestlist'),
    # ex: /weddings/5/vote/
    # url(r'^guest/(?P<guest_id>[0-9]+)/$', views.guestdetail, name='guestdetail'),
    url(r'^guest/(?P<pk>[0-9]+)/$', views.GuestDetailView.as_view(), name='guestdetail'),
    # url(r'^guest/new/$', views.NewGuestView.as_view(), name='guest-new'),
    url(r'^(?P<pk>[0-9]+)/guests/new/$', views.GuestAddView.as_view(),name='guest-add'),
]