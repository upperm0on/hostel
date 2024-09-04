from django.shortcuts import render, redirect, HttpResponse
from .models import Consumer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .views_create_consumer import Views_create_consumer

# Create your views here.
def create_consumer(request):
    forms = Views_create_consumer()
    if request.method == "POST":
        forms = Views_create_consumer(request.POST)
        if forms.is_valid(): 
            forms = Views_create_consumer()
            return redirect('/consumer/read_consumer/')
    context = {
        'forms': forms,
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