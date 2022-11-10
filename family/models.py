from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)