from django.shortcuts import get_object_or_404, render
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

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

class GuestListView(generic.DetailView):
    model = Event
    template_name = 'events/guestlist.html'

class GuestDetailView(generic.DetailView):
    model = Guest
    template_name = 'guests/detail.html'
