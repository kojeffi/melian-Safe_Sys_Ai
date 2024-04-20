from django.db import models

class SafetyIncident(models.Model):
    timestamp = models.DateTimeField()
    description = models.TextField()

class ComplianceRegulation(models.Model):
    regulation_number = models.CharField(max_length=50)
    description = models.TextField()

class EquipmentMaintenance(models.Model):
    equipment_name = models.CharField(max_length=100)
    maintenance_date = models.DateField()
    maintenance_description = models.TextField()
