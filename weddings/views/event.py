from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from weddings.models import Event, Guest

# def index(request):
#     latest_event_list = Event.objects.order_by('-date')[:5]
#     context = {'latest_event_list': latest_event_list}
#     return render(request, 'events/index.html', context)

# class IndexView(generic.ListView):
#     template_name = 'events/index.html'
#     context_object_name = 'latest_event_list'

#     def get_queryset(self):
#         """Return the last five events"""
#         return Event.objects.all()
class EventListView(generic.ListView):
    model = Event

@method_decorator(login_required, name='dispatch')
class EventNewView(generic.CreateView):
    model = Event
    fields = [ 'name', 'description', 'schedule', 'venue', 'address', 'latitude', 'longitude', 'date' ]
    success_url = reverse_lazy('weddings:event-list')

@method_decorator(login_required, name='dispatch')
class EventEditView(generic.UpdateView):
    model = Event
    fields = [ 'name', 'description', 'schedule', 'venue', 'address', 'latitude', 'longitude', 'date' ]
    success_url = reverse_lazy('weddings:event-list')

@method_decorator(login_required, name='dispatch')
class EventDeleteView(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('weddings:event-list')
    # template_name = 'events/event_confirm_delete.html'

class EventDetailView(generic.DetailView):
    model = Event

@method_decorator(login_required, name='dispatch')
class GuestListView(generic.DetailView):
    model = Event
    template_name = 'weddings/guest_list.html'