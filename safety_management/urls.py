from rest_framework.routers import DefaultRouter
from .views import AIDrivenSafetyManagementViewSet

router = DefaultRouter()
router.register(r'ai-driven-safety-management', AIDrivenSafetyManagementViewSet, basename='ai-driven-safety-management')
urlpatterns = router.urls


from django.urls import path
from .views import ai_driven_safety_management

urlpatterns = [
    path('ai-driven-safety-management/', ai_driven_safety_management, name='ai-driven-safety-management'),
    path('api/ai-driven-safety-management/', AIDrivenSafetyManagementViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/ai-driven-safety-management/<int:pk>/', AIDrivenSafetyManagementViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/ai-driven-safety-management/get-chart-data/', AIDrivenSafetyManagementViewSet.as_view({'get': 'get_chart_data'})),
    path('api/ai-driven-safety-management/update-data-entry/', AIDrivenSafetyManagementViewSet.as_view({'post': 'update_data_entry'})),
]
