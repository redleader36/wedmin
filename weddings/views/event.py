from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.db.models import Sum

from weddings.models import Event, Guest, GuestEvent, Registry, Lodging

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
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Event.objects.all()
        elif 'pin_provided' in self.request.session and 'logged_pin' in self.request.session:
            guest = self.check_pin(self.request.session['logged_pin'])
            if guest != False:
                print(guest.events.all())
                return guest.events.all()
        else:
             return Event.objects.filter(public=True)

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['registries'] = Registry.objects.all()
        context['lodging'] = Lodging.objects.all()
        # And so on for more models
        return context

    def check_pin(self, pin):
        try:
            return Guest.objects.get(invite_code__iexact=pin)
        except Guest.DoesNotExist:
            return False
        except Guest.MultipleObjectsReturned:
            return False

@method_decorator(login_required, name='dispatch')
class EventNewView(generic.CreateView):
    model = Event
    fields = [ 'name', 'description', 'schedule', 'venue', 'address', 'map_link', 'map_embed', 'date', 'date_end', 'public' ]
    success_url = reverse_lazy('weddings:event-list')

@method_decorator(login_required, name='dispatch')
class EventEditView(generic.UpdateView):
    model = Event
    fields = [ 'name', 'description', 'schedule', 'venue', 'address', 'map_link', 'map_embed', 'date', 'date_end', 'public' ]
    success_url = reverse_lazy('weddings:event-list')

@method_decorator(login_required, name='dispatch')
class EventDeleteView(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('weddings:event-list')
    # template_name = 'events/event_confirm_delete.html'

class EventDetailView(generic.DetailView):
    model = Event

@method_decorator(login_required, name='dispatch')
class GuestListView(generic.ListView):
    # model = Event
    template_name = 'weddings/guest_list.html'
    context_object_name = 'guestevent_list'

    def get_queryset(self):
        self.event = get_object_or_404(Event, pk=self.kwargs.get("pk"))
        guestevents = GuestEvent.objects.filter(event=self.event).select_related()
        totals = {}
        totals['invites'] = guestevents.count()
        totals['answered'] = guestevents.exclude(attending__isnull=True).count()
        totals['unanswered'] = totals['invites'] - totals['answered']
        totals['percent'] = "{:.1%}".format(totals['answered'] / totals['invites'])
        dict_totals = guestevents.exclude(attending__isnull=True).aggregate(Sum('adults'), Sum('children'))
        totals['adults'] = dict_totals['adults__sum']
        totals['children'] = dict_totals['children__sum']
        totals['combined'] = dict_totals['adults__sum'] + dict_totals['children__sum']
        self.totals = totals
        return guestevents

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GuestListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['event'] = self.event
        context['totals'] = self.totals
        return context

