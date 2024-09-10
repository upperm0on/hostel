from django.shortcuts import render, redirect

from .models import Hostel
from .add_hostel_forms import Views_addHostel


import json
# Create your views here.

def add_hostel(request): 
    form = Views_addHostel() 
    if request.method == "POST": 
        form = Views_addHostel(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            hidden_data = json.loads(request.POST['hidden_data'])
            print(form.cleaned_data, hidden_data)
            form = Views_addHostel()
    context = {
        'form' : form,
    }
    return render(request, 'hq/add_hostel.html', context)

def read_hostel(request): 
    hostels = Hostel.objects.all()
    context = {
        'hostels': hostels,
    }
    return render(request, 'hq/read_hostels.html', context)

def update_hostel(request, id):
    hostel_instance = Hostel.objects.get(id=id) 
    form = Views_addHostel(request.POST or None, instance=hostel_instance)
    if request.method == "POST":
        if form.is_valid(): 
            form.save()
            return redirect('/hq/read_hostel/')
    context = {
        'form' : form, 
    }
    return render(request, 'hq/update_hostel.html', context)