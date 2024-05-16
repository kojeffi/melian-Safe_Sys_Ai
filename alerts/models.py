from django.db import models

class SafetyIncident(models.Model):
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    severity = models.CharField(max_length=20)
   
class IncidentAnalytics(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

class Incident:
    objects = None