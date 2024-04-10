# views.py (core/views.py)
from django.shortcuts import render
from .models import Asset, SensorData, Compliance
from django.utils import timezone
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def home(request):
    assets = Asset.objects.all()
    compliances = Compliance.objects.filter(completed=False)
    context = {'assets': assets, 'compliances': compliances}
    return render(request, 'dashboard/predictive_maintenance.html', context)


def asset_detail(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    sensor_data = SensorData.objects.filter(asset=asset).order_by('-timestamp')[:100]

    # Real-Time Threat Detection
    latest_data = sensor_data.first()
    if latest_data.temperature > 100 or latest_data.pressure > 1000:
        alert = 'High temperature or pressure detected!'
    else:
        alert = None

    # Predictive Maintenance
    data = pd.DataFrame(list(sensor_data.values()))
    X = data[['temperature', 'pressure', 'vibration']]
    y = data['timestamp']
    model = RandomForestRegressor()
    model.fit(X, y)
    future_timestamps = model.predict(X)
    maintenance_due = future_timestamps.min() < timezone.now()

    context = {'asset': asset, 'sensor_data': sensor_data, 'alert': alert, 'maintenance_due': maintenance_due}
    return render(request, 'dashboard/predictive_maintenance.html', context)