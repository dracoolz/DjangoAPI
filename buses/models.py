from django.db import models
#Relation
from groups.models import Groups
class Buses(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)