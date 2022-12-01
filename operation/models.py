from django.db import models
#Relation
from buses.models import Buses
class Operation(models.Model):
    start = models.BooleanField(blank=False, unique=True)
    end = models.BooleanField(blank=False, unique=True)
    bus_id = models.ForeignKey(Buses, on_delete=models.CASCADE, unique=True)
    created = models.DateTimeField(auto_now_add=True)