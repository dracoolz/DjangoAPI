from django.db import models
#Relation
from buses.models import Buses
class Operation(models.Model):
    start = models.BooleanField(blank=False, default='')
    end = models.BooleanField(blank=False, default='')
    bus_id = models.ForeignKey(Buses, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)