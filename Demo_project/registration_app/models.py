from django.db import models

# Create your models here.

class Employee_Detial(models.Model):
    fname = models.CharField(max_length=20,null= True,blank=True)
    lname = models.CharField(max_length=20,null= True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null= True,blank=True)