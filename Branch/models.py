from django.db import models
class Branchlist(models.Model):
    courierid=models.IntegerField(default=250)
    name=models.CharField(max_length=250)
    pincode=models.IntegerField(default=250)
    district=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    