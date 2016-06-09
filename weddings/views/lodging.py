from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from weddings.models import Lodging

@method_decorator(login_required, name='dispatch')
class LodgingNewView(generic.CreateView):
    model = Lodging
    fields = [ 'name', 'description', 'url', 'address', 'map_link', 'map_embed', 'phone' ]
    success_url = reverse_lazy('weddings:event-list')

@method_decorator(login_required, name='dispatch')
class LodgingEditView(generic.UpdateView):
    model = Lodging
    fields = [ 'name', 'description', 'url', 'address', 'map_link', 'map_embed', 'phone' ]
    success_url = reverse_lazy('weddings:event-list')

@method_decorator(login_required, name='dispatch')
class LodgingDeleteView(generic.DeleteView):
    model = Lodging
    success_url = reverse_lazy('weddings:event-list')