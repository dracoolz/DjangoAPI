from django.db import models
#Relation
from buses.models import Buses
class Operation(models.Model):
    start = models.BooleanField(blank=False)
    end = models.BooleanField(blank=False)
    bus = models.ForeignKey(Buses, on_delete=models.CASCADE, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)