# views.py
from django.shortcuts import render, redirect
from .forms import SafetyRiskForm, ComplianceRegulationForm, EquipmentMaintenanceForm
from .models import SafetyRisk, ComplianceRegulation, EquipmentMaintenance

def real(request):
    safety_risks = SafetyRisk.objects.all()
    compliance_regulations = ComplianceRegulation.objects.all()
    equipment_maintenance = EquipmentMaintenance.objects.all()

    safety_risk_form = SafetyRiskForm(request.POST or None)
    compliance_regulation_form = ComplianceRegulationForm(request.POST or None)
    equipment_maintenance_form = EquipmentMaintenanceForm(request.POST or None)

    if request.method == 'POST':
        if safety_risk_form.is_valid():
            safety_risk_form.save()
            return redirect('realtime:real-url')
        elif compliance_regulation_form.is_valid():
            compliance_regulation_form.save()
            return redirect('realtime:real-url')
        elif equipment_maintenance_form.is_valid():
            equipment_maintenance_form.save()
            return redirect('realtime:real-url')

    context = {
        'safety_risks': safety_risks,
        'compliance_regulations': compliance_regulations,
        'equipment_maintenance': equipment_maintenance,
        'safety_risk_form': safety_risk_form,
        'compliance_regulation_form': compliance_regulation_form,
        'equipment_maintenance_form': equipment_maintenance_form,
    }
    return render(request, 'dashboard/realtime.html', context)
