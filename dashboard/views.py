from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SafetyIncidentForm, ComplianceRegulationForm, EquipmentMaintenanceForm
from .models import SafetyIncident, ComplianceRegulation, EquipmentMaintenance

def dashboard(request):
    safety_incidents = SafetyIncident.objects.all()
    compliance_regulations = ComplianceRegulation.objects.all()
    equipment_maintenance = EquipmentMaintenance.objects.all()

    safety_incident_form = SafetyIncidentForm(request.POST or None)
    compliance_regulation_form = ComplianceRegulationForm(request.POST or None)
    equipment_maintenance_form = EquipmentMaintenanceForm(request.POST or None)

    if request.method == 'POST':
        if safety_incident_form.is_valid():
            safety_incident_form.save()
            messages.success(request, 'Safety incident added successfully!')

        if compliance_regulation_form.is_valid():
            compliance_regulation_form.save()
            messages.success(request, 'Compliance regulation added successfully!')

        if equipment_maintenance_form.is_valid():
            equipment_maintenance_form.save()
            messages.success(request, 'Equipment maintenance record added successfully!')

        # Count the number of alerts
        alert_count = len(messages.get_messages(request))

        return redirect('dashboard')

    # Initial alert count
    alert_count = len(messages.get_messages(request))

    context = {
        'safety_incidents': safety_incidents,
        'compliance_regulations': compliance_regulations,
        'equipment_maintenance': equipment_maintenance,
        'safety_incident_form': safety_incident_form,
        'compliance_regulation_form': compliance_regulation_form,
        'equipment_maintenance_form': equipment_maintenance_form,
        'alert_count': alert_count,  #Pass alert count to template context
    }
    return render(request, 'dashbord/dashboard.html', context)