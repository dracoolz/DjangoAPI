from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=200,blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    driver = models.BooleanField(blank=False, default='')
    serial_number = models.IntegerField(blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)