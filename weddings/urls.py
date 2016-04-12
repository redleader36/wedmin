from django.conf.urls import url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

from . import views

app_name='weddings'
urlpatterns = [
    # event model
    url(r'^$', views.EventListView.as_view(), name='event-list'),
    url(r'^new/$', views.EventNewView.as_view(), name='event-new'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.EventDeleteView.as_view(), name='event-delete'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.EventEditView.as_view(), name='event-edit'),
    url(r'^(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(), name='event-detail'),
    # guest model
    url(r'^(?P<pk>[0-9]+)/guests/$', views.GuestListView.as_view(), name='guest-list'),
    url(r'^guest/(?P<pk>[0-9]+)/$', views.GuestDetailView.as_view(), name='guest-detail'),
    url(r'^(?P<pk>[0-9]+)/guest/new/$', views.GuestNewView.as_view(),name='guest-new'),
    url(r'^guest/(?P<pk>[0-9]+)/delete/$', views.GuestDeleteView.as_view(), name='guest-delete'),
    url(r'^guest/(?P<pk>[0-9]+)/edit/$', views.GuestEditView.as_view(), name='guest-edit'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'weddings\login.html'},name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': reverse_lazy('weddings:event-list')}, name='logout'),
]