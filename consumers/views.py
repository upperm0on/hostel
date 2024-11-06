from django.shortcuts import render, redirect, HttpResponse
from .models import Consumer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
 
# Create your views here.
def create_consumer(request):

    context = {
    }
    return render(request, 'consumer/create_consumer.html', context)

def read_consumer(request):
    objects = Consumer.objects.all()
    context = {
        'obj' : objects,
    }
    return render(request, 'consumer/read_consumer.html', context)


def delete_consumer(request):
    context = {}
    return render(request, 'consumer/delete_consumer.html', context)