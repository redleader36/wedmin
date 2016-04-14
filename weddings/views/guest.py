from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.utils.crypto import get_random_string

from weddings.models import Event, Guest

@method_decorator(login_required, name='dispatch')
class GuestDetailView(generic.DetailView):
    model = Guest
    # template_name = 'guests/detail.html'

@method_decorator(login_required, name='dispatch')
class GuestNewView(generic.CreateView):
    model = Guest
    fields = [ 'first_name', 'last_name', 'first_name_2', 'last_name_2', 'primary_email', 'street_address', 'street_address_2', 'city', 'state', 'zip_code', 'side', 'relation' ]
    # success_url = reverse_lazy('weddings:guestlist', kwargs={'pk': pk})
    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('weddings:guest-list', self.object.event.id)
    def get_success_url(self):
        event = self.object.event
        return reverse_lazy( 'weddings:guest-list', kwargs={'pk': event.id})

    def dispatch(self, *args, **kwargs):
        self.event = get_object_or_404(Event, pk=kwargs.get('pk', None))
        return super(GuestNewView, self).dispatch(*args, **kwargs)  

    def form_valid(self, form):
        form.instance.event = self.event
        form.instance.invite_code = get_random_string(6)
        return super(GuestNewView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class GuestEditView(generic.UpdateView):
    model = Guest
    fields = [ 'first_name', 'last_name', 'first_name_2', 'last_name_2', 'primary_email', 'street_address', 'street_address_2', 'city', 'state', 'zip_code', 'side', 'relation' ]
    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        event = self.object.event
        return reverse_lazy( 'weddings:guest-list', kwargs={'pk': event.id})

@method_decorator(login_required, name='dispatch')
class GuestDeleteView(generic.DeleteView):
    model = Guest
    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        event = self.object.event
        return reverse_lazy( 'weddings:guest-list', kwargs={'pk': event.id})