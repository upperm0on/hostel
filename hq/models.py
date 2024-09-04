from django.db import models
from managers.models import Manager


# Create your models here.
class Hostel(models.Model): 
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5000, decimal_places=2, default=0.00)
    location = models.CharField(max_length=50) 
    # ratings = models.ForeignKey()
    status_choices = [('Available', 'Available'), ('Unavailable', 'Unavailable')]
    status = models.CharField(choices=status_choices, max_length=50)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    # picture = models.ImageField()