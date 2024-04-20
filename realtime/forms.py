from django import forms
from .models import SafetyRisk, ComplianceRegulation, EquipmentMaintenance


class SafetyRiskForm(forms.ModelForm):
    class Meta:
        model = SafetyRisk
        fields = ['risk_name', 'risk_description', 'risk_level', 'risk_category']
        labels = {
            'risk_name': 'Risk Name',
            'risk_description': 'Risk Description',
            'risk_level': 'Risk Level',
            'risk_category': 'Risk Category'
        }
        help_texts = {
            'risk_name': 'Enter a descriptive name for the safety risk.',
            'risk_description': 'Provide detailed information about the safety risk.',
            'risk_level': 'Select the severity level of the safety risk.',
            'risk_category': 'Choose a category to classify the safety risk.'
        }


class ComplianceRegulationForm(forms.ModelForm):
    class Meta:
        model = ComplianceRegulation
        fields = ['regulation_name', 'regulation_description', 'regulation_category']
        labels = {
            'regulation_name': 'Regulation Name',
            'regulation_description': 'Regulation Description',
            'regulation_category': 'Regulation Category'
        }
        help_texts = {
            'regulation_name': 'Enter the name or title of the compliance regulation.',
            'regulation_description': 'Provide details about the compliance regulation requirements.',
            'regulation_category': 'Select a category to classify the compliance regulation.'
        }


class EquipmentMaintenanceForm(forms.ModelForm):
    class Meta:
        model = EquipmentMaintenance
        fields = ['equipment_name', 'maintenance_schedule', 'maintenance_description']
        labels = {
            'equipment_name': 'Equipment Name',
            'maintenance_schedule': 'Maintenance Schedule',
            'maintenance_description': 'Maintenance Description'
        }
        help_texts = {
            'equipment_name': 'Enter the name or identifier of the equipment requiring maintenance.',
            'maintenance_schedule': 'Select the scheduled date for equipment maintenance.',
            'maintenance_description': 'Describe the type of maintenance required or the reason for maintenance.'
        }
