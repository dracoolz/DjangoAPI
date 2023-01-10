from django.db import models
from buses.models import Buses
class Groups(models.Model):
    name = models.CharField(max_length=70, blank=False, unique=True)
    address = models.CharField(max_length=200,blank=False, null=True)
    buses_id = models.ForeignKey(Buses, on_delete=models.CASCADE, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)