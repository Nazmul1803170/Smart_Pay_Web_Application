from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null= True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    cardid = models.CharField(max_length=100,null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True,default=0)
    

    def __str__(self):
        return  self.name
    

class Trip(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null= True)
    start_lat = models.CharField(max_length=100)
    start_lon = models.CharField(max_length=100)
    end_lat = models.CharField(max_length=100,null= True, blank=True)
    end_lon = models.CharField(max_length=100,null= True, blank=True)
    distance = models.CharField(max_length=100,null= True, blank=True)
    bus_id = models.CharField(max_length=100, default=None,null=True,blank=True)

class Bus(models.Model):
    bus_id = models.CharField(max_length=100)
    bus_name = models.CharField(max_length=100)
    balance = models.IntegerField(null=True, blank=True,default=0)
    

  
