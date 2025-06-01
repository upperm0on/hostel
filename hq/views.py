from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
import os, requests

from django.db.models.signals import post_save
from django.dispatch import receiver


from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Hostel
from .add_hostel_forms import Views_addHostel
from ratings.models import (
    five_star,
    four_star,
    three_star,
    two_star,
    one_star
)

from managers.models import Manager

import json

from reviews.models import Reviews


def add_hostel(request):
    form = Views_addHostel()
    if request.method == "POST":
        form = Views_addHostel(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            hidden_data = request.POST.get('hidden_data', '[]')  # Default to empty list JSON

            try:
                room_details = json.loads(hidden_data)
                print("Parsed room details:", room_details)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
                room_details = []

            instance.room_details = hidden_data
            instance.additional_details = request.POST.get('hidden_info_data', '')
            manager = Manager.objects.get(user=request.user)

            instance.manager = manager

            room_images = request.FILES.getlist('room_image')
            print("Room images:", room_images)

            count = 0
            for room_image in room_images:
                room_number = str(room_details[count]['number_in_room']) if isinstance(room_details, list) and count < len(room_details) else str(count)

                room_image_path = os.path.join(settings.MEDIA_ROOT, 'room_images', instance.name, room_number)
                os.makedirs(room_image_path, exist_ok=True)

                try:
                    image_path = os.path.join(room_image_path, room_image.name)
                    with open(image_path, 'wb+') as destination:
                        for chunk in room_image.chunks():
                            destination.write(chunk)
                    print(f"Image saved at: {image_path}")
                except Exception as e:
                    print(f"Error saving image {room_image.name}: {e}")

                count += 1

            instance.save()
            return redirect('read_hostels')

    return render(request, 'hq/add_hostel.html', {'form': form})

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
    if request.method == "POST":
        form = Views_addHostel(request.POST, request.FILES, instance=hostel_instance)
        if form.is_valid():
            instance = form.save(commit=False)
            hidden_data = request.POST.get('hidden_data', '[]')  # Default to empty list JSON

            try:
                room_details = json.loads(hidden_data)
                print("Parsed room details:", room_details)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
                room_details = []

            instance.room_details = hidden_data
            instance.additional_details = request.POST.get('hidden_info_data', '')
            manager = Manager.objects.get(user=request.user)

            instance.manager = manager

            room_images = request.FILES.getlist('room_image')
            print(request.FILES)
            print("Room images:", room_images)

            count = 0
            for room_image in room_images:
                room_number = str(room_details[count]['number_in_room']) if isinstance(room_details, list) and count < len(room_details) else str(count)

                room_image_path = os.path.join(settings.MEDIA_ROOT, 'room_images', instance.name, room_number)
                os.makedirs(room_image_path, exist_ok=True)  # Ensure the directory exists

                try:
                    image_path = os.path.join(room_image_path, room_image.name)
                    with open(image_path, 'wb+') as destination:
                        for chunk in room_image.chunks():
                            destination.write(chunk)
                    print(f"Image saved at: {image_path}")
                    count += 1  # Increment the count only after successful processing
                except Exception as e:
                    print(f"Error saving image {room_image.name}: {e}")
                
            instance.save()
            return redirect('/hq/read_hostel/')
    else:
        form = Views_addHostel(instance=hostel_instance)
    context = {
        'form': form,
        'model': hostel_instance,
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
    hostel_name = slugify(hostel.name)  # Slugify the hostel name to replace spaces with hyphens

    manager = None
    
    try: 
        if request.user.is_authenticated:
            manager = Manager.objects.get(user=request.user)
    except: 
        pass

    reviews = Reviews.objects.filter(hostel=hostel).order_by('-created_at')

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
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
        'reviews': reviews,
        'manager': manager,
    }
    return render(request, template_name, context)

from consumers.models import Consumer
from payments.models import Payment
from django.utils.text import slugify

@csrf_exempt
def confirm_payment(request):
    if not request.user.is_authenticated:
        return redirect('signin')  # Redirect to signin if user is not authenticated

    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)  # ✅ Store request body separately
            print("✅ Received Data in Backend:", request_data)

            paystack_reference = request_data.get('reference')
            hostel_id = request_data.get('hostel_id')
            room_id = request_data.get('room_id')
            amount_paid = float(request_data.get('amount', 0.00))

            if not paystack_reference:
                print("❌ Reference is missing!")
                return JsonResponse({"success": False, "message": "No transaction reference provided."}, status=400)

            print(f"✅ Verifying transaction with Paystack for reference: {paystack_reference}")
            url = f"https://api.paystack.co/transaction/verify/{paystack_reference}"
            headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
            response = requests.get(url, headers=headers)
            paystack_data = response.json()  # ✅ Store Paystack response separately

            print("✅ Paystack Response:", paystack_data)

            if not paystack_data.get("status") or paystack_data.get("data") is None:
                print("❌ Invalid response from Paystack")
                return JsonResponse({"success": False, "message": "Invalid response from Paystack."}, status=400)

            if paystack_data["data"].get("status") != "success":
                print("❌ Payment verification failed.")
                return JsonResponse({"success": False, "message": "Payment verification failed."}, status=400)

            amount_verified = float(paystack_data["data"].get("amount", 0)) / 100  # Convert from kobo
            if amount_verified != amount_paid:
                print("❌ Mismatched amount: Expected", amount_paid, "but got", amount_verified)
                return JsonResponse({"success": False, "message": "Payment amount mismatch."}, status=400)

            print(f"✅ Payment verified successfully for reference: {paystack_reference}")

            consumer = Consumer()
            consumer.user = request.user
            consumer.room_id = room_id
            consumer.hostel = Hostel.objects.get(id=hostel_id)
            consumer.amount = request_data.get('amount')
            consumer.save()

            return JsonResponse({
                "success": True,
                "message": "Payment verified successfully.",
                "transaction_id": paystack_reference,
                "amount_paid": amount_paid
            }, status=200)

        except Exception as e:
            print("❌ Backend Error:", str(e))
            return JsonResponse({"success": False, "message": str(e)}, status=500)

    return redirect('/dashboard/')

@receiver(post_save, sender=Consumer)
def create_transaction_for_consumer(sender, instance, created, **kwargs):
    room_details = json.loads(instance.hostel.room_details)
    room = next((room for room in room_details if str(room.get("number_in_room")) == str(instance.room_id)), {}),
    if created:
        Payment.objects.create(
            consumer=instance,
            amount = instance.amount,
        )
        print(f"✅ Transaction created for consumer {instance.id}")
