from django.db import models

# Create your models here.


class Employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    password =models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    salary = models.IntegerField(null=True,blank=True)