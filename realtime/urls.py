# urls.py
from django.urls import path
from . import views

app_name = 'realtime'

urlpatterns = [
    path('', views.real, name='real-url'),
]