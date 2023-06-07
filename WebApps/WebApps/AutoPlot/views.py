from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import AutoPlot_model

# Create your views here.
def AutoPlot(request):
    
    events = AutoPlot_model.objects.all().values()
    template = loader.get_template('AutoPlot.html')
    context = {
    'events': events,
    }
    return HttpResponse(template.render(context, request))