from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


from .forms import PostForm # new
from .models import VolunteerEvent
from django.contrib.auth.models import User


def login(request):
    if not request.user.is_authenticated:
        return render(request, 'volunteer/login.html', None)

    return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))


def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    return render(request, 'volunteer/index.html', None)


def myschedule(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    me=request.user.events_attending.all()

    ids_past = [event.id for event in me if event.is_past()]
    events_past = me.filter(id__in=ids_past)
    events_upcoming = me.exclude(id__in=ids_past)

    context={'events_upcoming': events_upcoming, 'events_past': events_past}
    print("CONTEXT", context)
    return render(request, 'volunteer/myschedule.html', context)

def myevents(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    me=request.user.events_written.all()

    ids_past = [event.id for event in me if event.is_past()]
    events_past = me.filter(id__in=ids_past)
    events_upcoming = me.exclude(id__in=ids_past)

    context={'events_upcoming': events_upcoming, 'events_past': events_past}
    print("CONTEXT", context)
    return render(request, 'volunteer/myevents.html', context)

class CreateVolunteerEventView(LoginRequiredMixin ,generic.CreateView):
    model = VolunteerEvent
    form_class = PostForm
    template_name = 'volunteer/createpost.html'
    # success_url = reverse_lazy('volunteer:createpost')
    def get_success_url(self):
        return reverse_lazy('volunteer:createpost')

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = PostForm
        form = self.get_form(form_class)

        if (form.is_valid()):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """

        obj = form.save(commit=False)
        obj.event_author = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form, articleimage_form, articletag_form,
                        articlecategory_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(self.get_context_data(form=form))


class EventBrowseView(LoginRequiredMixin ,generic.ListView):
    template_name = 'volunteer/eventbrowse.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        # return VolunteerEvent.objects.order_by('-event_title')

        return VolunteerEvent.objects.filter(event_datetime__gt=timezone.now())

def unregister(request, pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    if (request.method == 'POST'):
        VolunteerEvent.objects.get(pk=pk).attending.remove(request.user)

        return HttpResponseRedirect(reverse_lazy('volunteer:myschedule'))
    else: 
        return render(request, 'volunteer/eventbrowse.html')


def signup(request, pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    if (request.method=="POST"):
        #VolunteerProfile.eventlist.append(event_title)
        #VolunteerProfile.eventlist=[event_title]
        #user = User.objects.get(id=request.user.id)  
        #user.profile.events.add(VolunteerEvent.objects.get(event_title=event_title))
        #user.profile.numofevents+=1
        #profile.eventlist.append(event_title)
        #request.user.VolunteerProfile.events.add(event_title)
        #num=VolunteerProfile.numofevents
        #VolunteerProfile.numofevents=VolunteerProfile.numofevents+1
        #VolunteerEvent.objects.get(event_title=event_title).attending.add(request.user)
        VolunteerEvent.objects.get(pk=pk).attending.add(request.user)
        print(request.user.events_attending.all())

        return HttpResponseRedirect(reverse_lazy('volunteer:myschedule'))
    else: 
        return render(request, 'volunteer/eventbrowse.html')

class MyScheduleView(LoginRequiredMixin, generic.ListView):
    template_name='volunteer/schedule.html'
    context_object_name='me'
    #print("EVENTS ATTENDING: ")
    #print(User.events_attending.all())
    def get_queryset(self):
        print("In view: ", me)
        return me



class DetailView(LoginRequiredMixin, generic.DetailView):
    model = VolunteerEvent
    template_name = 'volunteer/detail.html'

    def get_context_data(self, **kwargs):
        event_id = self.kwargs['pk'] # the event being detailed
        registered_events = self.request.user.events_attending.all()
        registered = registered_events.filter(id=event_id).exists() # check if contained in user's events

        context = super().get_context_data(**kwargs)
        context['registered'] = registered
        return context

class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = VolunteerEvent
    template_name = 'volunteer/detailmyevent.html'
