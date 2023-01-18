from django.db import models
#Relation
from operation.models import Operation
from users.models import Users
class Passenger(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, blank=True, null=True, default=None)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    status = models.BooleanField(blank=False, unique=False)
    created = models.DateTimeField(auto_now_add=True)