from django.urls import path
from . import views

app_name = 'realtime'

urlpatterns = [
    path('real', views.real, name='real-url'),
    path('', views.anomaly_detection, name='anomaly_detection'),  # URL for anomaly detection view
    path('predictive-maintenance/', views.predictive_maintenance, name='predictive_maintenance'),
    # URL for predictive maintenance view
    path('api/anomaly-results/', views.anomaly_results_api, name='anomaly-results-api'),
    # Add other URL patterns here if needed
]
