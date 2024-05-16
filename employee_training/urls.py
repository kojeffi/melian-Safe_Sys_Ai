from django.urls import path
from . import views

urlpatterns = [
    path('training-resources/', views.training_resources, name='training_resources'),
    path('resource/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('resource/<int:resource_id>/mark-completed/', views.mark_resource_completed, name='mark_completed'),
]