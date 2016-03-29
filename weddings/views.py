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

# def detail(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)
#     return render(request, 'events/detail.html', {'event': event})

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

# def guestlist(request, event_id):
#     guest_list = Guest.objects.filter(event=event_id)
#     event = Event.objects.filter(id=event_id)
#     # guest_list={}
#     # for s in Guest.SIDE_OPTIONS:
#     #     relation_list={}
#     #     for r in Guest.RELATION_OPTIONS:
#     #         # guest_list = { s[1] : r[1] }
#     #         list = Guest.objects.filter(event=event_id, side=s[0], relation=r[0])
#     #         relation_list.update({r[1] : list })
#     #     guest_list.update({s[1] : relation_list })
#     context = {'guest_list': guest_list, 'relation_options' : Guest.RELATION_OPTIONS, 'side_options': Guest.SIDE_OPTIONS, 'event' : event}
#     return render(request, 'events/guestlist.html', context )

# def guestlist(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)
#     return render(request, 'events/guestlist.html', {'event': event})

class GuestListView(generic.DetailView):
    model = Event
    template_name = 'events/guestlist.html'

# def guestdetail(request, guest_id):
#     guest = get_object_or_404(Guest, pk=guest_id)
#     return render(request, 'guests/detail.html', {'guest': guest})

class GuestDetailView(generic.DetailView):
    model = Guest
    template_name = 'guests/detail.html'
