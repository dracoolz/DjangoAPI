from django.db import models
from django import forms
# Relation one to many
from groups.models import Groups
from family.models import Family
class Users(models.Model):
    name = models.CharField(max_length=70, blank=False)
    email = models.CharField(max_length=200,blank=False)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    driver = models.BooleanField(blank=False)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    family_id = models.ForeignKey(Family, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)