
# views.py
from django.shortcuts import render
from .models import SafetyRisk, ComplianceRegulation, EquipmentMaintenance

def real(request):
    safety_risks = SafetyRisk.objects.all()
    compliance_regulations = ComplianceRegulation.objects.all()
    equipment_maintenance = EquipmentMaintenance.objects.all()
    context = {
        'safety_risks': safety_risks,
        'compliance_regulations': compliance_regulations,
        'equipment_maintenance': equipment_maintenance,
    }
    return render(request, 'dashboard/realtime.html', context)
