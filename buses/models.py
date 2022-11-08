from django.db import models

class Buses(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    group_id = models.CharField(max_length=70, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)