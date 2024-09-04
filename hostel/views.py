from django.shortcuts import render

def dashboard(request):
    template_name = "dashboard.html"
    context = {}
    return render(request, template_name, context)

def landingPage(request): 
    template_name = "landingPage.html"
    context = {}
    return render(request, template_name, context)