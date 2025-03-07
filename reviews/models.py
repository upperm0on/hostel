from django.db import models
from django.contrib.auth.models import User
from hq.models import Hostel


# Create your models here.
class Reviews(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=True, blank=True) 
    review = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
