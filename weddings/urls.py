from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from . import views

app_name='weddings'
urlpatterns = [
    # event model
    url(r'^$', views.Invite1View.as_view(), name='invite1'),
    # url(r'^invite/(?P<pk>[0-9]+)/$', views.Invite2View.as_view(), name='invite2'),
    url(r'^invite/(?P<slug>\w+)/$', views.Invite2View.as_view(), name="invite2"),
    url(r'^events/$', views.EventListView.as_view(), name='event-list'),
    url(r'^events/new/$', views.EventNewView.as_view(), name='event-new'),
    url(r'^events/(?P<pk>[0-9]+)/delete/$', views.EventDeleteView.as_view(), name='event-delete'),
    url(r'^events/(?P<pk>[0-9]+)/edit/$', views.EventEditView.as_view(), name='event-edit'),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(), name='event-detail'),
    # guest model
    url(r'^events/(?P<pk>[0-9]+)/guests/$', views.GuestListView.as_view(), name='guest-list'),
    url(r'^guest/(?P<pk>[0-9]+)/$', views.GuestDetailView.as_view(), name='guest-detail'),
    url(r'^events/(?P<pk>[0-9]+)/guest/new/$', views.GuestNewView.as_view(),name='guest-new'),
    url(r'^guest/(?P<pk>[0-9]+)/delete/$', views.GuestDeleteView.as_view(), name='guest-delete'),
    url(r'^guest/(?P<pk>[0-9]+)/edit/$', views.GuestEditView.as_view(), name='guest-edit'),
    url(r'^login/$', auth_views.login, {'template_name': 'weddings/login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': reverse_lazy('weddings:event-list')}, name='logout'),
]