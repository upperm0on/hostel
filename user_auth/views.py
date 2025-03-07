from django.shortcuts import render, redirect, HttpResponse
from .view_forms import View_user_login, View_user_signup
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .models import Account_status

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your views here.
def user_signup(request):
    template = 'user_login/login.html'
    message = 'Sign Up Here'
    forms = View_user_signup() 
    if request.method == "POST":
        forms = View_user_signup(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['name']
            email = forms.cleaned_data['email']
            password = forms.cleaned_data['password']

            user = User.objects.create(username=username, email=email) 
            user.set_password(password)
            user.save()

            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect('/dashboard/')
    context = {
        'forms' : forms,
        'msg': message,
    }
    return render(request, template, context)

@receiver(post_save, sender=User)
def create_account_status(sender, instance, created, **kwargs):
    if created:  # Only run when a new user is created
        Account_status.objects.create(user=instance)

def user_login(request):
    template = 'user_login/login.html'
    message = 'Login Here'
    error_msg = ''
    forms = View_user_login() 
    if request.method == "POST":
        forms = View_user_login(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['name']
            password = forms.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect('/dashboard/')
            else: 
                error_msg = 'The Username or Password was invalid or not found in the database'
    context = {
        'forms' : forms,
        'msg': message,
        'error_msg': error_msg,
    }
    return render(request, template, context)

def user_logout(request):
    logout(request)
    return redirect('landing_page')
    

