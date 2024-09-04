from django.shortcuts import render
from .create_manager_forms import Views_create_manager
from .models import Manager

# Create your views here.
def create_manager(request):
    forms = Views_create_manager() 
    if request.method == "POST": 
        forms = Views_create_manager(request.POST)
        if forms.is_valid(): 
            print(forms.cleaned_data)
    context = {
        'forms' : forms,
    }
    return render(request, 'manager/create_manager.html', context)

def read_manager(request):
    managers = Manager.objects.all()
    context = {
        'obj': managers,
    }
    return render(request, 'manager/read_manager.html', context)

def update_manager(request, id):
    instance = Manager.objects.get(id=id)
    forms = Views_create_manager(instance=instance) 
    if request.method == "POST": 
        forms = Views_create_manager(request.POST)
        if forms.is_valid(): 
            print(forms.cleaned_data)
    context = {
        'forms' : forms,
    }
    return render(request, 'manager/update_manager.html', context)

def delete_manager(request):
    context = {}
    return render(request, 'manager/delete_manager.html', context)