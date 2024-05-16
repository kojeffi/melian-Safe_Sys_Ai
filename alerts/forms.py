from django import forms
from .models import SafetyIncident


class SafetyIncidentForm(forms.ModelForm):
    class Meta:
        model = SafetyIncident
        fields = ['description', 'location', 'severity']
