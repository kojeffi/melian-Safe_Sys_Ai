# safety/views.py
import random

from django.shortcuts import render, redirect
from .models import SensorData, SafetyAlert


def index(request):
    # Simulate some recent safety alerts (replace with actual logic)
    recent_alerts = SafetyAlert.objects.order_by('-created_at')[:5]
    context = {'recent_alerts': recent_alerts}
    return render(request, 'safety/index.html', context)


def simulate_sensor_data(request):
    # Simulate receiving sensor data (replace with real data source)
    # Generate random sensor data
    sensor_type = random.choice(['temperature', 'pressure', 'vibration'])
    value = random.random() * 100
    data = SensorData.objects.create(sensor_type=sensor_type, value=value)

    # Simulate triggering an alert based on pre-defined conditions (replace with actual logic)
    if value > 80:
        message = f"High {sensor_type} detected! Potential safety hazard."
        SafetyAlert.objects.create(message=message)

    # Render a confirmation template instead of redirecting
    context = {'message': 'Sensor data simulated successfully!'}
    return render(request, 'safety/simulation_confirmation.html', context)
