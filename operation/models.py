from django.db import models

class Operation(models.Model):
    start = models.BooleanField(blank=False, default='')
    end = models.BooleanField(blank=False, default='')
    bus_id = models.IntegerField(blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)