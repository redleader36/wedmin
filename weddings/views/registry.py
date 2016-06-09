from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from weddings.models import Registry

@method_decorator(login_required, name='dispatch')
class RegistryNewView(generic.CreateView):
    model = Registry
    fields = [ 'name', 'description', 'url', 'image' ]
    success_url = reverse_lazy('weddings:event-list')

@method_decorator(login_required, name='dispatch')
class RegistryEditView(generic.UpdateView):
    model = Registry
    fields = [ 'name', 'description', 'url', 'image' ]
    success_url = reverse_lazy('weddings:event-list')

@method_decorator(login_required, name='dispatch')
class RegistryDeleteView(generic.DeleteView):
    model = Registry
    success_url = reverse_lazy('weddings:event-list')