from django.db import models
from consumers.models import Consumer

import datetime
# Create your models here.
class Payment(models.Model): 
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(default=datetime.datetime.now())

    def get_amount(self): 
        return self.amount