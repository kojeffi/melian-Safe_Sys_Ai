from django.contrib import admin
from django.urls import path, include
from . import views as my_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_views.home, name='home-url'),
    path('auth/', include('auth.urls')),
    path('alerts/', include('alerts.urls')),
    path('realtime/', include('realtime.urls')),

]
