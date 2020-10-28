from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy

from .forms import PostForm # new
from .models import VolunteerEvent


def login(request):
    return render(request, 'volunteer/login.html', None)


def index(request):
    # template = loader.get_template('volunteer/index.html')
    # return HttpResponse(template.render())
    return render(request, 'volunteer/index.html', None)


def myschedule(request):
    return render(request, 'volunteer/myschedule.html', None)

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