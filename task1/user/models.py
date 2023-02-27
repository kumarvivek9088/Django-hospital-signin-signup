from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profilepic = models.FileField()
    line1 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profilepic = models.FileField()
    line1 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    
    