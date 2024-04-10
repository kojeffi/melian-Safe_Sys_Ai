# models.py (core/models.py)
from django.db import models


class Asset(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)


class SensorData(models.Model):
    objects = None
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    pressure = models.FloatField()
    vibration = models.FloatField()


class Compliance(models.Model):
    objects = None
    regulation = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)