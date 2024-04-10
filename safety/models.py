# safety/models.py

from django.db import models


class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor_type = models.CharField(max_length=50)
    value = models.FloatField()


class SafetyAlert(models.Model):
    objects = None
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor_type = models.CharField(max_length=50, blank=True)  # Optional: sensor type
    sensor_value = models.FloatField(blank=True, null=True)  # Optional: sensor value
    severity_level = models.CharField(max_length=10, choices=[('HIGH', 'High'), ('MEDIUM', 'Low')], default='LOW')
    acknowledged = models.BooleanField(default=False)  # Flag to track if alert is acknowledged


# safety/models.py

from django.db import models

class AIModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Define other fields specific to your AI model here
