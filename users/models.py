from django.db import models
from django import forms
# Relation one to many
from groups.models import Groups
from family.models import Family
class Users(models.Model):
    name = models.CharField(max_length=70, blank=False)
    email = models.CharField(max_length=200, blank=False, unique=True)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    driver = models.BooleanField(blank=True, null=True)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    family_id = models.ForeignKey(Family, on_delete=models.CASCADE, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)