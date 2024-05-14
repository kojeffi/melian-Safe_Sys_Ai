from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views as my_views
from .views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_views.home, name='home-url'),
    path('alerts/', include('alerts.urls')),
    path('realtime/', include('realtime.urls')),
    path('user_app/', include('user_app.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('employee_training/', include('employee_training.urls')),
    path('about/', my_views.about, name='about-url'),
    path('acceptable/', my_views.acceptable, name='acceptable-url'),
    path('accessibility/', my_views.accessibility, name='accessibility-url'),
    path('contact/', my_views.contact, name='contact-url'),
    path('features/', my_views.features, name='features-url'),
    path('privacy/', my_views.privacy, name='privacy-url'),
    path('services/', my_views.services, name='services-url'),
    path('terms/', my_views.terms, name='terms-url'),
    path('contact/', contact, name='contact'),
]

# Add media URL patterns to serve profile photos during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
