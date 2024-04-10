# urls.py
from django.urls import path
from . import views

app_name = 'safesys'

urlpatterns = [
    path('', views.dashboard, name='safe-url'),
]
