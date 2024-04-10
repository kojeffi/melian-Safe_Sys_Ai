# dashboard/views.py
from django.shortcuts import render, redirect
from .models import SafetyIncident
from .forms import SafetyIncidentForm


def alerts(request):
    incidents = SafetyIncident.objects.all()
    return render(request, 'alerts/index.html', {'incidents': incidents})


def create_incident(request):
    if request.method == 'POST':
        form = SafetyIncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alerts:alert-url')
    else:
        form = SafetyIncidentForm()
    return render(request, 'alerts/create_incident.html', {'form': form})


# alerts/views.py
from django.http import JsonResponse
from .models import Incident


def real_time_analytics(request):
    # Perform analytics computations (example: count incidents by severity)
    analytics_data = {
        'total_incidents': Incident.objects.count(),
        'high_severity_count': Incident.objects.filter(severity='High').count(),
        'medium_severity_count': Incident.objects.filter(severity='Medium').count(),
        'low_severity_count': Incident.objects.filter(severity='Low').count(),
    }
    return JsonResponse(analytics_data)

