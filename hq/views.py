from django.shortcuts import render, redirect

from .models import Hostel
from .add_hostel_forms import Views_addHostel
from ratings.models import (
    five_star,
    four_star,
    three_star,
    two_star,
    one_star
)

import json
# Create your views here.

def add_hostel(request): 
    form = Views_addHostel() 
    if request.method == "POST": 
        form = Views_addHostel(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            hidden_data = request.POST['hidden_data']
            add_info_data = request.POST['hidden_info_data']
            
            instance.room_details = hidden_data
            instance.additional_details = add_info_data
            instance.save()
            print(form.cleaned_data, hidden_data, add_info_data)
            form = Views_addHostel()
    context = {
        'form' : form,
    }
    return render(request, 'hq/add_hostel.html', context)


def read_hostel(request): 
    hostels = Hostel.objects.all().order_by("-ratings")
    
    stars_list = [one_star, two_star, three_star, four_star, five_star]  # List of star rating models

    for obj in hostels: 
        total_star = 0 
        count2 = 0
    # Calculate the total star rating and count
        for i in range(len(stars_list)):
            count = stars_list[i].objects.filter(product=obj).count()
            counted_rate = stars_list[i].objects.filter(product=obj).count()
            count2 += counted_rate

            count = count * (i + 1) 
            total_star += count

        # Calculate the average rating
        try: 
            total_rate = (total_star/count2) 
        except: 
            total_rate = 0

        obj.ratings = round(total_rate, 1)
        obj.save()
    
        print(obj, obj.ratings) 

    context = {
        'hostels': hostels,
    }
    return render(request, 'hq/read_hostels.html', context)

def update_hostel(request, id):
    hostel_instance = Hostel.objects.get(id=id) 
    form = Views_addHostel(request.POST or None, request.FILES,  instance=hostel_instance)
    if request.method == "POST":
        if form.is_valid(): 
            form.save()
            return redirect('/hq/read_hostel/')
    context = {
        'form' : form, 
    }
    return render(request, 'hq/update_hostel.html', context)

def search_hostel(request, rooms): 
    template_name = "hq/search_hostels.html"
    objects = Hostel.objects.all().order_by("-ratings")
    queryset = list()
    for obj in objects:
        if obj.room_details: 
            room_details = json.loads(obj.room_details)
            for room in room_details: 
                if int(room["number_in_room"]) == int(rooms): 
                    print(obj.name)
                    query = Hostel.objects.get(id=obj.id)
                    queryset.append(query) 
    context = {
        'hostels' : queryset,
    }
    return render(request, template_name, context)

def detail_hostel(request, id): 
    template_name = 'hq/detail_hostel.html'
    hostel = Hostel.objects.get(id=id) 
    context = {
        'hostel': hostel,
    }
    return render(request, template_name, context)