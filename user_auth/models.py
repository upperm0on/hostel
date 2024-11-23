from django.db import models

from managers.models import Manager
from django.contrib.auth.models import User

# Create your models here.

class Account_status(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ACCOUNT_STATUS_CHOICES = [('consumer', 'consumer'), ('manager', 'manager')]
    user_status = models.CharField(max_length=255, choices=ACCOUNT_STATUS_CHOICES, default='consumer', blank=True, null=True)