from django.shortcuts import render, HttpResponse as response
from hq.models import Hostel
from django.contrib.auth.decorators import login_required
from user_auth.models import Account_status
from consumers.models import Consumer
from managers.models import Manager

from payments.models import Payment

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
                consumers = Consumer.objects.filter(hostel__manager=manager).count()

                context['hostel_consumers_number'] = consumers
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