from django.db import models

class Groups(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    address = models.CharField(max_length=200,blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)