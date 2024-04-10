# urls.py (core/urls.py)
from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('asset/<int:asset_id>/', views.asset_detail, name='asset_detail'),
]
