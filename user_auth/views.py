from django.shortcuts import render, redirect, HttpResponse
from .view_forms import View_user_login, View_user_signup
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def user_signup(request):
    template = 'user_login/login.html'

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
    }
    return render(request, template, context)

def user_login(request):
    template = 'user_login/login.html'

    forms = View_user_login() 
    if request.method == "POST":
        forms = View_user_login(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect('/dashboard/')
            print(user)
    context = {
        'forms' : forms,
    }
    return render(request, template, context)

