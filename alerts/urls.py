from django.urls import path
from . import views as my_views

app_name = 'alerts'

urlpatterns = [
    path('alerts/', my_views.alerts, name='alert-url'),
    path('create_incident/', my_views.create_incident, name='create_incident'),
]
