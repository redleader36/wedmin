from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import Event, Guest

# def index(request):
#     latest_event_list = Event.objects.order_by('-date')[:5]
#     context = {'latest_event_list': latest_event_list}
#     return render(request, 'events/index.html', context)

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        """Return the last five events"""
        return Event.objects.all()

class NewEventView(generic.CreateView):
    model = Event
    fields = [ 'name', 'date']
    success_url = reverse_lazy('weddings:detail')
    template_name = 'events/event_form.html'

class EventDeleteView(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('weddings:index')
    template_name = 'events/event_confirm_delete.html'

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

class GuestListView(generic.DetailView):
    model = Event
    template_name = 'events/guestlist.html'

class GuestDetailView(generic.DetailView):
    model = Guest
    template_name = 'guests/detail.html'

