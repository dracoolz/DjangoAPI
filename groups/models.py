from django.db import models

class Groups(models.Model):
    name = models.CharField(max_length=70, blank=False, unique=True)
    address = models.CharField(max_length=200,blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)