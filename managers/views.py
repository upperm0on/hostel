from django.shortcuts import render, redirect
from .models import Manager
from user_auth.models import Account_status

# Create your views here.
def create_manager(request):
    if request.method == "POST": 
        if 'agree_manager' in request.POST: 
            acc = Account_status()
            acc.user = request.user
            acc.user_status = "manager"

            acc.save() 

            if acc.user_status == "manager": 
                man = Manager.objects.create(user=acc.user)
                man.save()

                return redirect('dashboard')        
    context = {}
    return render(request, 'manager/create_manager.html', context)

def read_manager(request):
    managers = Manager.objects.all()
    context = {
        'obj': managers,
    }
    return render(request, 'manager/read_manager.html', context)

def delete_manager(request):
    context = {}
    return render(request, 'manager/delete_manager.html', context)