from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Desigination(models.Model):
    desigination=models.CharField(max_length=100,null=True)

class registration(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    username=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    desigination=models.ForeignKey(Desigination,on_delete=models.CASCADE)

class VehicleRegistration(models.Model):
    VehicleNumber=models.CharField(max_length=255)
    VehicleModel=models.CharField(max_length=255)
    VehicleType=models.CharField(max_length=255)
    VehicleDescription=models.CharField(max_length=400)
    