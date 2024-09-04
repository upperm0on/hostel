from django.db import models
from hq.models import Hostel

# Create your models here.
class Consumer(models.Model): 
    name = models.CharField(max_length=244)
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=255)
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT, null=True, blank=True)