from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import Event, Guest

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

class EventNewView(generic.CreateView):
    model = Event
    fields = [ 'name', 'description', 'schedule', 'venue', 'address', 'latitude', 'longitude', 'date' ]
    success_url = reverse_lazy('weddings:event-list')

class EventEditView(generic.UpdateView):
    model = Event
    fields = [ 'name', 'description', 'schedule', 'venue', 'address', 'latitude', 'longitude', 'date' ]
    success_url = reverse_lazy('weddings:event-list')

class EventDeleteView(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('weddings:event-list')
    # template_name = 'events/event_confirm_delete.html'

class EventDetailView(generic.DetailView):
    model = Event

class GuestListView(generic.DetailView):
    model = Event
    template_name = 'weddings/guest_list.html'

class GuestDetailView(generic.DetailView):
    model = Guest
    # template_name = 'guests/detail.html'

class GuestNewView(generic.CreateView):
    model = Guest
    fields = [ 'first_name', 'last_name', 'first_name_2', 'last_name_2', 'primary_email', 'street_addr', 'city', 'state', 'zip_code', 'side', 'relation' ]
    # success_url = reverse_lazy('weddings:guestlist', kwargs={'pk': pk})
    def get_success_url(self, **kwargs):
        return reverse_lazy('weddings:guest-list', self.event.pk)

    def dispatch(self, *args, **kwargs):
        self.event = get_object_or_404(Event, pk=kwargs.get('pk', None))
        return super(GuestNewView, self).dispatch(*args, **kwargs)  

    def form_valid(self, form):
        form.instance.event = self.event
        return super(GuestNewView, self).form_valid(form)

class GuestEditView(generic.UpdateView):
    model = Guest
    fields = [ 'first_name', 'last_name', 'first_name_2', 'last_name_2', 'primary_email', 'street_addr', 'city', 'state', 'zip_code', 'side', 'relation' ]
    
    # def dispatch(self, *args, **kwargs):
    #     self.event = get_object_or_404(Event, pk=kwargs.get('pk', None))
    #     return super(GuestEditView, self).dispatch(*args, **kwargs)
    
    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('weddings:guest-list', self.event)

    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        event = self.object.event
        return reverse_lazy( 'weddings:guest-list', kwargs={'pk': event.id})

class GuestDeleteView(generic.DeleteView):
    model = Guest
    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        event = self.object.event
        return reverse_lazy( 'weddings:guest-list', kwargs={'pk': event.id})