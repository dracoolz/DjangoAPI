from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=70, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)