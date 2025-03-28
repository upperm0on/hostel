from django.shortcuts import render, HttpResponse as response
from hq.models import Hostel
from django.contrib.auth.decorators import login_required
from user_auth.models import Account_status
from consumers.models import Consumer
from managers.models import Manager

from payments.models import Payment

from django.conf import settings

from ratings.models import (
    five_star,
    four_star,
    three_star,
    two_star,
    one_star
)

import json
@login_required(login_url='/authenticate/login')
def dashboard(request):
    context = {}
    template_name = "dashboard.html"

    # Initialize manager and consumer context
    context['is_manager'] = False
    context['consumer'] = None

    try: 
        # Check if the user is a manager
        manager = Manager.objects.filter(user=request.user).first()
        if manager:
            context['is_manager'] = True
            hostel = Hostel.objects.filter(manager=manager).first()

            if hostel: 
                context['hostel'] = hostel
                hostel_users = Consumer.objects.filter(hostel=hostel)

                # Prepare room prices from hostel details
                # room_prices = {str(room_data['number_in_room']): int(room_data['price']) for room_data in json.loads(hostel.room_details)}

                payments = Payment.objects.filter(consumer__hostel__manager=manager)

                total_revenue = 0
                for payment in payments: 
                    total_revenue += payment.amount

                context['total_revenue'] = total_revenue
                manager = Manager.objects.get(user=request.user)
                consumers = Consumer.objects.filter(hostel__manager=manager)

                context['hostel_consumers_number'] = consumers.count()
                context['consumers'] = consumers
                context['hostel_consumers'] = hostel_users

                context['media_url'] = settings.MEDIA_URL

                room_details = Hostel.objects.get(manager=manager).room_details
                room_details = json.loads(room_details)
                
                payment_data = Payment.objects.filter(consumer__hostel__manager=manager)
                
                RevenueInsight = dict()

                for data in payment_data: 
                    month = data.timestamp.strftime("%B")[:3]
                    RevenueInsight[month] = RevenueInsight.get(month, 0) + data.amount

                # Convert the data map into a format suitable for Google Charts
                bookingTrendsDataList = [["Month", "Revenue"]]
                for month, revenue in RevenueInsight.items():
                    bookingTrendsDataList.append([month, revenue])

                # Pass the data as JSON to the context for use in JavaScript
                context['RevenueInsight'] = json.dumps(RevenueInsight)
                print(RevenueInsight)



                total_rooms = 0
                for i, detail in enumerate(room_details):
                    i = 1
                    total_rooms += i

                context['total_rooms'] = total_rooms
                stars_list = [one_star, two_star, three_star, four_star, five_star]

                total_star = 0
                total_ratings_count = 0
            

                for i, star_model in enumerate(stars_list):
                    star_count = star_model.objects.filter(product=hostel).count()
                    total_star += star_count * (i + 1)
                    total_ratings_count += star_count

                total_rate = total_star / total_ratings_count if total_ratings_count > 0 else 0

                context['ratings'] = round(total_rate, 1)
                filtered_consumers_dict = dict()
                for detail in room_details: 
                    filtered_consumers = consumers.filter(room_id=int(detail['number_in_room'])).count()
                    filtered_consumers_dict[detail['number_in_room']] = filtered_consumers

                    
                context['filtered_consumers_dict'] = json.dumps(filtered_consumers_dict)
            else: 
                context['err'] = "You do not have any hostel"

                
    except Manager.DoesNotExist:
        pass  # Not a manager

    try:
        # Check if the user is a consumer
        consumer = Consumer.objects.filter(user=request.user).first()
        if consumer:
            context['consumer'] = consumer
    except Consumer.DoesNotExist:
        pass  # Not a consumer

    # Recommended hostels for non-consumers
    if not context['consumer']:
        hostels = Hostel.objects.all().order_by('-ratings')
        context['hostels'] = hostels

    return render(request, template_name, context)


def landingPage(request): 
    template_name = "landingPage.html"
    context = {}
    return render(request, template_name, context)