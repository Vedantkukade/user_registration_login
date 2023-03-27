from django.db import models

# Create your models here.
class userregister(models.Model):
    username=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    dob=models.DateField()
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    phone_number=models.CharField(max_length=50)
