# from django.shortcuts import get_object_or_404
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, UpdateView
# from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext

from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from weddings.models import Event, Guest, CodeGuess, GuestEvent
# from weddings.forms import EventFormSet, GuestForm

class Invite1View(TemplateView):
    template_name = "weddings/invite1.html"
    error = False
    pin = None

    def get(self, request, *args, **kwargs):
        if 'pin_provided' in request.session and 'logged_pin' in request.session:
            guest = self.check_pin(request.session['logged_pin'])
            if guest != False:
                messages.success(request, "Code Accepted")
                return HttpResponseRedirect(reverse_lazy( 'weddings:invite2', kwargs={'slug': guest.invite_code.upper()}))

        if 'post_pin' in request.session:
            self.pin = request.session['post_pin'].strip()

        response = super(Invite1View, self).get(request, *args, **kwargs)
        return response

    def post(self, request):
        if 'pin' not in request.POST or request.POST['pin'].strip() == '':
            messages.error(request, 'Give the code')
            # log empty try of guess
            CodeGuess.objects.create(ip=self.ip_addr(request), guess_code='')
            return HttpResponseRedirect(reverse('weddings:invite1'))

        request.session['post_pin'] = request.POST['pin'].strip().upper()

        # check if there is not too much tries
        guesses = CodeGuess.objects.filter(when_tried__gt=datetime.today() - timedelta(hours=3), \
                                            ip=self.ip_addr(request))
        if len(guesses) > 30:
            CodeGuess.objects.create(ip=self.ip_addr(request), guess_code=request.POST['pin'])
            messages.error(request, 'That\'s it. You locked for next 3 hours')
            return HttpResponseRedirect(reverse('weddings:invite1'))

        # log guess trying
        CodeGuess.objects.create(ip=self.ip_addr(request), guess_code=request.POST['pin'])

        success_response = HttpResponseRedirect(reverse_lazy( 'weddings:invite2', kwargs={'slug': request.POST['pin'].upper()}))

        try:
            obj = Guest.objects.get(invite_code__iexact=request.POST['pin'].upper())

            request.session['logged_pin'] = obj.invite_code
            request.session['pin_provided'] = True
            messages.success(request, 'Code Approved')
        except Guest.DoesNotExist:
            messages.error(request, 'No such code')
            return HttpResponseRedirect(reverse('weddings:invite1'))
        except Guest.MultipleObjectsReturned:
            messages.error(request, 'No such code')
            return HttpResponseRedirect(reverse('weddings:invite1'))

        return success_response

    def get_context_data(self, **kwargs):
        context = super(Invite1View, self).get_context_data(**kwargs)
        context['error'] = self.error
        context['pin'] = self.pin
        return context

    def check_pin(self, pin):
        try:
            return Guest.objects.get(invite_code__iexact=pin)
        except Guest.DoesNotExist:
            return False
        except Guest.MultipleObjectsReturned:
            return False

    def ip_addr(self, request):
        if 'HTTP_X_REAL_IP' not in request.META:
            return request.META['REMOTE_ADDR']
        else:
            return request.META['HTTP_X_REAL_IP']

class InviteDetailView(DetailView):
    template_name = "weddings/invite-detail.html"
    model = Guest
    slug_field = 'invite_code'


# class Invite3View(UpdateView):
#     """
#         View to add a child to a family
#         url: /family/<family-slug>/add/child
#     """
#     model = Guest
#     form_class = GuestEditForm
#     context_object_name = 'guest'
#     template_name = 'weddings/invite3.html'

#     def get_initial(self):
#         """Calculate Initial Data for the form, validate ownership of family"""
#         family_slug = self.kwargs.get('slug', self.request.POST.get('slug'))
#         family = get_object_or_404(Family, slug=family_slug)
        
#         return {'family_slug': family_slug}

class GuestEventInline(InlineFormSet):
    model = GuestEvent
    fields = [ 'attending', 'adults', 'children' ]
    extra = 0
    can_delete=False

class Invite2View(UpdateWithInlinesView):
    template_name = "weddings/invite2.html"
    model = Guest
    inlines = [ GuestEventInline ]
    # inline_model = GuestEvent
    fields = []
    slug_field = 'invite_code'
    # form_class = GuestForm

    # def get_queryset(self):
    #    # query_set = super(ModelxUpdateView, self).get_queryset().filter(user=self.request.user)
    #    print(self.kwargs['invite_code'])
    #    guest_set = Guest.objects.get(invite_code=self.kwargs['invite_code'])
    #    query_set = guest_set.event_set.all()
    #    print(guest_set)
    #    print(query_set)
    #    return query_set 

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     event_form = EventFormSet(instance = self.object)
    #     return self.render_to_response(self.get_context_data(form = form, event_form = event_form))

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     event_form = EventFormSet(self.request.POST, instance=self.object)

    #     if (form.is_valid() and event_form.is_valid()):
    #       return self.form_valid(form, event_form)
    #     return self.form_invalid(form, event_form)

    # def form_valid(self, form, event_form):
    #     self.object = form.save()
    #     event_form.instance = self.object
    #     event_form.save()
    #     return HttpResponseRedirect(self.get_success_url())

    # def form_invalid(self, form, event_form):
    #     print("Form Invalid")
    #     return self.render_to_response(self.get_context_data(form=form, event_form=event_form))

    def get_success_url(self):
        # event = self.object.event
        return reverse_lazy( 'weddings:event-list' )


    # guest_list = None
    # logged_in_guest = 0
    # invited_guest_id = ""
    # invited_guest_fullname = ""

    # def get(self, request, *args, **kwargs):
    #     if 'logged_in_guest' in request.COOKIES:
    #         self.logged_in_guest = request.COOKIES['logged_in_guest']

    #     if 'pin_provided' in request.session and 'logged_pin' in request.session:
    #         invitation = self.check_pin(request.session['logged_pin'])
    #         if invitation != False:
    #             guests = invitation.weddingguest_set.filter(invited=False)
    #             self.guest_list = guests
    #             invited_guests = invitation.weddingguest_set.filter(invited=True)
    #             if len(invited_guests) > 0:
    #                 invitation_guest = invited_guests[0]
    #                 self.invited_guest_id = invitation_guest.pk
    #                 self.invited_guest_fullname = invitation_guest.full_name
    #             return super(Invite2View, self).get(request, *args, **kwargs)

    #     # in case something went worng
    #     return HttpResponseRedirect(reverse('weddings:invite1'))

    # # todo - check if lonely guest dont want to get friend
    # def post(self, request, *args, **kwargs):
    #     if 'pin_provided' not in request.session and 'logged_pin' not in request.session:
    #         return HttpResponseRedirect(reverse('weddings:invite1'))

    #     invitation = self.check_pin(request.session['logged_pin'])
    #     if invitation == False:
    #         return HttpResponseRedirect(reverse('weddings:invite1'))

    #     real_guests = invitation.weddingguest_set.filter(invited=False)
    #     real_guest_count = len(real_guests)
    #     if real_guest_count < 2:
    #         # Two cases. When there is only one WeddingGuest (invited = False)

    #         # get already invited guests
    #         invited_guests = invitation.weddingguest_set.filter(invited=True)

    #         # check if name was entered
    #         if 'invitation_guest_fullname' in request.POST and request.POST['invitation_guest_fullname'] != '':
    #             # guest fullname was provided
    #             provided_full_name = request.POST['invitation_guest_fullname'].strip()
    #             first_name = ""
    #             last_name = ""
    #             if len(provided_full_name.split(' ')) == 2:
    #                 first_name, last_name = provided_full_name.split(' ')
    #             elif len(provided_full_name.split(' ')) > 2:
    #                 first_name, last_name = provided_full_name.split(' ')[:2]
    #             else:
    #                 first_name = provided_full_name.strip()

    #             # if there is already invited guests lets update their fullname with provided now
    #             if len(invited_guests) > 0:
    #                 # save existing
    #                 invited_guest = invited_guests[0]
    #                 invited_guest.first_name = first_name
    #                 invited_guest.last_name = last_name
    #                 invited_guest.invited_by = real_guests[0]
    #                 invited_guest.save()
    #             else:
    #                 # create a new one
    #                 new_guest = WeddingGuest()
    #                 new_guest.invited = True
    #                 new_guest.invitation = invitation
    #                 new_guest.invited_by = real_guests[0]
    #                 new_guest.first_name = first_name
    #                 new_guest.last_name = last_name
    #                 new_guest.save()

    #         request.session['logged_in_guest'] = real_guests[0].pk

    #         response = HttpResponseRedirect(reverse('invitation'))

    #     else:
    #         # Second case. When it is more than one WeddingGuest (invited = False)
    #         if 'guest' not in request.POST or request.POST['guest'] == '':
    #             messages.error(request, "Choose guest from list below")
    #             return HttpResponseRedirect(reverse('weddings:invite2'))

    #         guests = invitation.weddingguest_set.all()
    #         allowed_guest_ids = [guest.id for guest in guests]

    #         guest_id = int(request.POST['guest'])

    #         if guest_id not in allowed_guest_ids:
    #             messages.error(request, "You kiddin ? You cannot choose this guest, something went wrong, call police")
    #             return HttpResponseRedirect(reverse('weddings:invite2'))

    #         request.session['logged_in_guest'] = guest_id

    #         response = HttpResponseRedirect(reverse('invitation'))
    #         response.set_cookie('logged_in_guest', guest_id)

    #     return response

    # def check_pin(self, pin):
    #     try:
    #         return Guest.objects.get(invite_code__iexact=pin)
    #     except Guest.DoesNotExist:
    #         return False

    # def get_context_data(self, **kwargs):
    #     context = super(Invite2View, self).get_context_data(**kwargs)
    #     context['guests'] = self.guest_list
    #     context['guest_count'] = len(self.guest_list)
    #     context['logged_in_guest'] = int(self.logged_in_guest)
    #     context['invitation_guest_id'] = self.invited_guest_id
    #     context['invitation_guest_fullname'] = self.invited_guest_fullname
    #     return context