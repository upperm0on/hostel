from django.db import models
from hq.models import Hostel as product

# Create your models here.
class five_star(models.Model): 
	product = models.ForeignKey(product, on_delete=models.CASCADE)

class four_star(models.Model): 
	product = models.ForeignKey(product, on_delete=models.CASCADE)

class three_star(models.Model): 
	product = models.ForeignKey(product, on_delete=models.CASCADE)

class two_star(models.Model): 
	product = models.ForeignKey(product, on_delete=models.CASCADE)

class one_star(models.Model): 
	product = models.ForeignKey(product, on_delete=models.CASCADE)