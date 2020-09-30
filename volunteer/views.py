from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    # template = loader.get_template('volunteer/index.html')
    # return HttpResponse(template.render())
    return render(request, 'volunteer/index.html', None)

def myschedule(request):
    return render(request, 'volunteer/myschedule.html', None)
