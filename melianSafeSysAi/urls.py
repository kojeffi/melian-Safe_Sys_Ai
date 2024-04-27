from django.contrib import admin
from django.urls import path, include

from . import views as my_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_views.home, name='home-url'),
    path('alerts/', include('alerts.urls')),
    path('realtime/', include('realtime.urls')),
    path('user_app/', include('user_app.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('employee_training/', include('employee_training.urls')),
    path('chat/', include('chat.urls')),
]
