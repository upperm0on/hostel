from django.shortcuts import render, HttpResponse as response
from hq.models import Hostel
from django.contrib.auth.decorators import login_required

from consumers.models import Consumer

@login_required(login_url='/authenticate/login')
def dashboard(request):
    context = dict()
    try: 
        consumer = Consumer.objects.get(user=request.user)
        if consumer: 
            context['consumer'] = consumer
    except: 
        hostels = Hostel.objects.all().order_by('-ratings')
        context['hostels'] = hostels
        print(request.session)
    context['hostels'] = Hostel.objects.all().order_by('-ratings')
    template_name = "dashboard.html"
    return render(request, template_name, context)

def landingPage(request): 
    template_name = "landingPage.html"
    context = {}
    return render(request, template_name, context)