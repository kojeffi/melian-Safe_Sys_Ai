from django.contrib import admin
from django.urls import path, include
from . import views as my_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_views.home, name='home-url'),
    path('auth/', include('auth.urls')),
    path('alerts/', include('alerts.urls')),
    path('safety_management/', include('safety_management.urls')),
    path('safety/', include('safety.urls')),
    path('safesys/', include('safesys.urls')),
    path('realtime/', include('realtime.urls')),
    path('core/', include('core.urls')),  # Corrected: added trailing slash after 'core/'
    path('about/', my_views.about, name='about-url'),
    path('quote/', my_views.quote, name='quote-url'),
    path('pricing/', my_views.pricing, name='pricing-url'),
    path('sample/', my_views.sample, name='sample-url'),
    path('servicedetails/', my_views.servicedetails, name='service-details-url'),
    path('services/', my_views.services, name='services-url'),
]
