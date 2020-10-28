from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy

from .forms import PostForm # new
from .models import VolunteerEvent
from django.contrib.auth.models import User


def login(request):
    return render(request, 'volunteer/login.html', None)


def index(request):
    # template = loader.get_template('volunteer/index.html')
    # return HttpResponse(template.render())
    return render(request, 'volunteer/index.html', None)


def myschedule(request):
    me=request.user.events_attending.all()
    context={'myevents': me}
    print("CONTEXT", context)
    return render(request, 'volunteer/myschedule.html', context)

class CreateVolunteerEventView(generic.CreateView):
    model = VolunteerEvent
    form_class = PostForm
    template_name = 'volunteer/createpost.html'
    success_url = reverse_lazy('volunteer:createpost')

    # model = VolunteerEvent
    # template_name = 'volunteer/createpost.html'
    # # fields = ['event_title', 'event_datetime', 'event_description', 'event_image']
    # fields = ['event_title', 'event_description']
    # success_url = reverse_lazy('volunteer:createpost') # use lazy to avoid circular import error


class EventBrowseView(generic.ListView):
    template_name = 'volunteer/eventbrowse.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return VolunteerEvent.objects.order_by('-event_title')


def signup(request, event_title):  
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
        VolunteerEvent.objects.get(event_title=event_title).attending.add(request.user)
        print(request.user.events_attending.all())

        return HttpResponseRedirect(reverse_lazy('volunteer:myschedule'))
    else: 
        return render(request, 'volunteer/eventbrowse.html')

class MyScheduleView(generic.ListView): 
    template_name='volunteer/schedule.html'
    context_object_name='me'
    #print("EVENTS ATTENDING: ")
    #print(User.events_attending.all())
    def get_queryset(self):
        print("In view: ", me)
        return me