from sqlite3 import Timestamp
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.EmailField(max_length=200,blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    driver = models.BooleanField(blank=False, default='')
    serial_number = models.IntegerField(blank=False, default='')
    timestamp = models.DateTimeField(auto_now_add=True)