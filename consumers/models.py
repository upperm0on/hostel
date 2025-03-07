from django.db import models
from hq.models import Hostel
from django.contrib.auth.models import User

# Create your models here.
class Consumer(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    room_id = models.IntegerField(blank=True, null=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=True, blank=True) 
    amount = models.DecimalField(max_digits=255, decimal_places=2, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)