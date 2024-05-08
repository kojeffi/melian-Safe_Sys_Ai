from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views as my_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_views.home, name='home-url'),
    path('alerts/', include('alerts.urls')),
    path('realtime/', include('realtime.urls')),
    path('user_app/', include('user_app.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('employee_training/', include('employee_training.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
