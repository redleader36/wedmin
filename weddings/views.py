from django.shortcuts import get_object_or_404, render

from .models import Event, Guest

def index(request):
    latest_event_list = Event.objects.order_by('-date')[:5]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'weddings/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'weddings/detail.html', {'event': event})

def list(request, event_id):
    response = "You're looking at the guest list of event %s."
    return HttpResponse(response % event_id)

def info(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    return render(request, 'weddings/info.html', {'guest': guest})
