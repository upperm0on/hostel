from django.shortcuts import render, redirect
from django.conf import settings
import os

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
            
            # Get the list of room images
            room_images = request.FILES.getlist('room_image')
            print(room_images) 
            
            # Parse hidden data if necessary
            room_details = json.loads(hidden_data)
            
            instance.room_details = hidden_data
            instance.additional_details = add_info_data
            
            for room_image in room_images:
                # Create the path for saving images
                room_image_path = os.path.join(settings.MEDIA_ROOT, 'room_images', instance.name, room_details['number_in_room'])
                os.makedirs(room_image_path, exist_ok=True)  # Create directory if it doesn't exist
                
                # Save the image
                try:
                    with open(os.path.join(room_image_path, room_image.name), 'wb+') as destination:
                        for chunk in room_image.chunks():
                            destination.write(chunk)
                except Exception as e:
                    print(f"Error saving image {room_image.name}: {e}")
                    # Optionally handle the error (e.g., log it or notify the user)
            
            instance.save()  # Save the hostel instance after processing
            # Redirect or render a success message as needed
            return redirect('read_hostels')  # Update with the actual URL
            
    context = {
        'form': form,
    }
    return render(request, 'hq/add_hostel.html', context)


def read_hostel(request): 
    hostels = Hostel.objects.all().order_by("-ratings")
    
    stars_list = [one_star, two_star, three_star, four_star, five_star]  

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

        try: 
            total_rate = (total_star/count2) 
        except: 
            total_rate = 0

        obj.ratings = round(total_rate, 1)
        obj.save()
    
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
    queryset = []

    for obj in objects:
        try:
            if obj.room_details: 
                room_details = json.loads(obj.room_details)
                
                for room in room_details:
                    if int(room.get("number_in_room", 0)) == int(rooms):  # Use .get to avoid KeyError
                        print(obj.name)
                        queryset.append(obj)  # Append obj directly instead of re-querying
                        break  # Stop inner loop once a match is found for efficiency
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error parsing room details for hostel {obj.name}: {e}")
            continue  # Skip this hostel if there's a JSON parsing or value error

    context = {
        'hostels': queryset,
    }
    return render(request, template_name, context)


def detail_hostel(request, id): 
    template_name = 'hq/detail_hostel.html'
    hostel = Hostel.objects.get(id=id)
    hostel_name = hostel.name  # Replace with your logic to get the hostel name

    print(hostel.room_details)

    room_image_urls = []
    for room in json.loads(hostel.room_details):
        room_number = room['number_in_room'] # Replace with your logic to get the room number
        image_directory = os.path.join(settings.MEDIA_ROOT, 'room_images', hostel_name, room_number)

        if os.path.exists(image_directory):
            for filename in os.listdir(image_directory):
                if filename.endswith(('.png', '.jpg', '.jpeg')):
                    room_image_urls.append(os.path.join(settings.MEDIA_URL, 'room_images', hostel_name, room_number, filename))
                    
    print(room_image_urls)
    context = {
        'hostel': hostel,
        'room_images': room_image_urls,
    }
    return render(request, template_name, context)

def room_details(request, name): 
    template_name = 'hq/room_detail.html'
    context = {}
    return render(request, template_name, context)