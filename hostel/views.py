from django.shortcuts import render
from hq.models import Hostel

def dashboard(request):
    hostels = Hostel.objects.all().order_by('-ratings')
    template_name = "dashboard.html"
    context = {
        'hostels': hostels,
    }
    return render(request, template_name, context)

def landingPage(request): 
    template_name = "landingPage.html"
    context = {}
    return render(request, template_name, context)