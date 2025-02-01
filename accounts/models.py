import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
    ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)    #TODO:get dropdown choices
    annual_income = models.PositiveIntegerField(null=True, blank=True)