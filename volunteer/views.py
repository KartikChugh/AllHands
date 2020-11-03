from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


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

class CreateVolunteerEventView(LoginRequiredMixin ,generic.CreateView):
    model = VolunteerEvent
    form_class = PostForm
    template_name = 'volunteer/createpost.html'
    success_url = reverse_lazy('volunteer:createpost')

    # model = VolunteerEvent
    # template_name = 'volunteer/createpost.html'
    # # fields = ['event_title', 'event_datetime', 'event_description', 'event_image']
    # fields = ['event_title', 'event_description']
    # success_url = reverse_lazy('volunteer:createpost') # use lazy to avoid circular import error


class EventBrowseView(LoginRequiredMixin ,generic.ListView):
    template_name = 'volunteer/eventbrowse.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return VolunteerEvent.objects.order_by('-event_title')


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



class DetailView(LoginRequiredMixin ,generic.DetailView):
    model = VolunteerEvent
    template_name = 'volunteer/detail.html'
