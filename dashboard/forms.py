from django import forms
from .models import SafetyIncident, ComplianceRegulation, EquipmentMaintenance

class SafetyIncidentForm(forms.ModelForm):
    class Meta:
        model = SafetyIncident
        fields = ['timestamp', 'description']
        widgets = {
            'timestamp': forms.DateInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'timestamp': 'Timestamp',
            'description': 'Description'
        }
        help_texts = {
            'timestamp': 'Select the date and time of the safety incident.',
            'description': 'Provide a detailed description of the safety incident.'
        }

class ComplianceRegulationForm(forms.ModelForm):
    class Meta:
        model = ComplianceRegulation
        fields = ['regulation_number', 'description']
        widgets = {
            'regulation_number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'regulation_number': 'Regulation Number',
            'description': 'Description'
        }
        help_texts = {
            'regulation_number': 'Enter the number or code of the compliance regulation.',
            'description': 'Provide details about the compliance regulation requirements.'
        }

class EquipmentMaintenanceForm(forms.ModelForm):
    class Meta:
        model = EquipmentMaintenance
        fields = ['equipment_name', 'maintenance_date', 'maintenance_description']
        widgets = {
            'equipment_name': forms.TextInput(attrs={'class': 'form-control'}),
            'maintenance_date': forms.DateInput(attrs={'class': 'form-control'}),
            'maintenance_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'equipment_name': 'Equipment Name',
            'maintenance_date': 'Maintenance Date',
            'maintenance_description': 'Maintenance Description'
        }
        help_texts = {
            'equipment_name': 'Enter the name or identifier of the equipment requiring maintenance.',
            'maintenance_date': 'Select the scheduled date for equipment maintenance.',
            'maintenance_description': 'Describe the type of maintenance required or the reason for maintenance.'
        }