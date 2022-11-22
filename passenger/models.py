from django.db import models
#Relation
from operation.models import Operation
from users.models import Users
class Passenger(models.Model):
    operation_id = models.ForeignKey(Operation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.BooleanField(blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)