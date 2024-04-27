# models.py
from django.db import models


class SafetyRisk(models.Model):
    risk_name = models.CharField(max_length=255)
    risk_description = models.TextField()
    risk_level = models.IntegerField()
    risk_category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ComplianceRegulation(models.Model):
    regulation_name = models.CharField(max_length=255)
    regulation_description = models.TextField()
    regulation_category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EquipmentMaintenance(models.Model):
    equipment_name = models.CharField(max_length=255)
    maintenance_schedule = models.DateField()
    maintenance_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AnomalyResult:
    objects = None
