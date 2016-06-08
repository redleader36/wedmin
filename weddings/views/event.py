from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from weddings.models import Event, Guest, Registry, Lodging

# def EventListView(request):
# #     event_list = Event.objects.order_by('-date')[:5]
#     if request.user.is_authenticated():
#         return Event.objects.all()
#     else:
#         return Event.objects.filter(public=True) 
#     context = {'event_list': event_list}
#     return render(request, 'weddings/event_list.html', context)

# class IndexView(generic.ListView):
#     template_name = 'events/index.html'
#     context_object_name = 'latest_event_list'

#     def get_queryset(self):
#         """Return the last five events"""
#         return Event.objects.all()

class EventListView(generic.ListView):
    # def get_queryset(self):
    #     if request.user.is_authenticated():
    #         return Event.objects.all()
    #     else:
    #         return Event.objects.filter(public=True)    
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['registries'] = Registry.objects.all()
        context['lodging'] = Lodging.objects.all()
        # And so on for more models
        return context

@method_decorator(login_required, name='dispatch')
class EventNewView(generic.CreateView):
    model = Event
    fields = [ 'name', 'description', 'schedule', 'venue', 'address', 'map_link', 'map_embed', 'date', 'public' ]
    success_url = reverse_lazy('weddings:event-list')

@method_decorator(login_required, name='dispatch')
class EventEditView(generic.UpdateView):
    model = Event
    fields = [ 'name', 'description', 'schedule', 'venue', 'address', 'map_link', 'map_embed', 'date', 'public' ]
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