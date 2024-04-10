from django.urls import path
from . import views

app_name = 'safety'  # Enclose URL patterns within an app namespace

urlpatterns = [
    path('safety_index/', views.index, name='safety_index'),
    path('simulate/', views.simulate_sensor_data, name='simulate_sensor_data'),
]
