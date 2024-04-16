from django import forms
from .models import SafetyRisk, ComplianceRegulation, EquipmentMaintenance

class SafetyRiskForm(forms.ModelForm):
    class Meta:
        model = SafetyRisk
        fields = ['risk_name', 'risk_description', 'risk_level', 'risk_category']

class ComplianceRegulationForm(forms.ModelForm):
    class Meta:
        model = ComplianceRegulation
        fields = ['regulation_name', 'regulation_description', 'regulation_category']

class EquipmentMaintenanceForm(forms.ModelForm):
    class Meta:
        model = EquipmentMaintenance
        fields = ['equipment_name', 'maintenance_schedule', 'maintenance_description']
