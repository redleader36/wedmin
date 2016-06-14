from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.utils.crypto import get_random_string

from weddings.models import Event, Guest, GuestEvent

@method_decorator(login_required, name='dispatch')
class GuestDetailView(generic.DetailView):
    model = Guest
    # template_name = 'guests/detail.html'

@method_decorator(login_required, name='dispatch')
class GuestNewView(generic.CreateView):
    model = Guest
    fields = [ 'first_name', 'last_name', 'first_name_2', 'last_name_2', 'email', 'street_address', 'street_address_2', 'city', 'state', 'zip_code', 'events', 'side', 'relation' ]
    # def get_success_url(self):
    #     event = self.object.event
    #     return reverse_lazy( 'weddings:guest-list', kwargs={'pk': events.id})
    def get_success_url(self):
        return reverse('weddings:guest-detail',args=(self.object.id,))

    # def dispatch(self, *args, **kwargs):
    #     self.events = get_object_or_404(Event, pk=kwargs.get('pk', None))
    #     return super(GuestNewView, self).dispatch(*args, **kwargs)  

    def form_valid(self, form):
        # form.instance.events = self.events
        form.instance.invite_code = get_random_string(4, allowed_chars='ABCDEFGHJKLMNPQRSTUVWXYZ23456789')
        # messages.success(self.request, 'New Guest Created!')
        return super(GuestNewView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class GuestEditView(generic.UpdateView):
    model = Guest
    fields = [ 'first_name', 'last_name', 'first_name_2', 'last_name_2', 'email', 'street_address', 'street_address_2', 'city', 'state', 'zip_code', 'events', 'side', 'relation' ]
    # def get_success_url(self):
    #     # Assuming there is a ForeignKey from Comment to Post in your model
    #     events = self.object.events
    #     return reverse_lazy( 'weddings:guest-list', kwargs={'pk': events.id})
    def get_success_url(self):
        return reverse('weddings:guest-detail',args=(self.object.id,))

@method_decorator(login_required, name='dispatch')
class GuestDeleteView(generic.DeleteView):
    model = Guest
    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        # event = self.object.event
        # return reverse_lazy( 'weddings:guest-list', kwargs={'pk': event.id})
        # Todo: change success url to last viewed guest list
        return reverse('weddings:event-list')
