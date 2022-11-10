from django.db import models

class Passenger(models.Model):
    operation_id = models.IntegerField(blank=False, default='')
    user_id = models.IntegerField(blank=False, default='')
    status = models.BooleanField(blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)