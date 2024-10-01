from django.db import models
class Listlist(models.Model):
    receivername=models.CharField(max_length=250)
    sendername=models.CharField(max_length=250)
    pickupaddress=models.CharField(max_length=250)
    deliveryaddress=models.CharField(max_length=250)
    weight=models.IntegerField(default=250)
    cost=models.IntegerField(default=250)



# Create your models here.
