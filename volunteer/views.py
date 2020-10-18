from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import VolunteerEvent


def index(request):
    # template = loader.get_template('volunteer/index.html')
    # return HttpResponse(template.render())
    return render(request, 'volunteer/index.html', None)

def myschedule(request):
    return render(request, 'volunteer/myschedule.html', None)

class CreateVolunteerEventView(generic.CreateView):
    model = VolunteerEvent
    template_name = 'volunteer/createpost.html'
    fields = ['event_title', 'event_datetime']
# def createpost(request):
#     return render(request, 'volunteer/createpost.html', None)
