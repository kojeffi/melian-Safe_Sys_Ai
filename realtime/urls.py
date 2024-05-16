from django.urls import path
from . import views

app_name = 'realtime'

urlpatterns = [
    path('real', views.real, name='real-url'),
    path('', views.anomaly_detection, name='anomaly_detection'),
    path('predictive-maintenance/', views.predictive_maintenance, name='predictive_maintenance'),
    path('api/anomaly-results/', views.anomaly_results_api, name='anomaly-results-api'),
]
