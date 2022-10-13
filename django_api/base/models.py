from email.policy import default
from lib2to3.pgen2 import driver
from turtle import end_fill
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class buses(models.Model):
    numberPlate = models.CharField(max_length=200)
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class buses_user(models.Model):
    userId = models.CharField(max_length=200)
    busId = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200, default='')
    driver = models.BooleanField(null=False)
    serial_number = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
