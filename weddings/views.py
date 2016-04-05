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
    fields = [ 'name', 'date']
    success_url = reverse_lazy('weddings:detail')

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

class GuestAddView(generic.CreateView):
    model = Guest
    fields = [ 'first_name', 'last_name', 'first_name_2', 'last_name_2', 'attending', 'primary_email', 'street_addr', 'city', 'state', 'zip_code', 'side', 'relation' ]
    # success_url = reverse_lazy('weddings:guestlist', kwargs={'pk': pk})
    def get_success_url(self, **kwargs):
        return reverse_lazy('weddings:guestlist', self.event.pk)


    def dispatch(self, *args, **kwargs):
        self.event = get_object_or_404(Event, pk=kwargs.get('pk', None))
        return super(GuestAddView, self).dispatch(*args, **kwargs)  

    def form_valid(self, form):
        form.instance.event = self.event
        return super(GuestAddView,self).form_valid(form)

    

