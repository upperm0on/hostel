from django.db import models
from hq.models import Hostel
from django.contrib.auth.models import User

# Create your models here.
class Consumer(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    account_list = [('user', 'user'), ('manager', 'manager')]

    account_type = models.CharField(max_length=255, default='user', choices=account_list)