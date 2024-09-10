from django.db import models
from managers.models import Manager
from category.models import Category

# Create your models here.
class Hostel(models.Model): 
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50) 
    # ratings = models.ForeignKey()
    status_choices = [('Available', 'Available'), ('Unavailable', 'Unavailable')]
    status = models.CharField(choices=status_choices, max_length=50)
    additional_details = models.JSONField(null=True, blank=True)
    room_details = models.JSONField(null=True, blank=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)