from django.conf import settings
from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)