from django.db import models
#Relation
from operation.models import Operation
from users.models import Users
class Passenger(models.Model):
    operation_id = models.ForeignKey(Operation, on_delete=models.CASCADE, unique=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, unique=True)
    status = models.BooleanField(blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)