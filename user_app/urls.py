from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register-url'),
    path('login/', views.user_login, name='login-url'),
    path('dashboard/', views.dashboard, name='dashboard-url'),
    path('profile/', views.profile, name='profile-url'),
    path('contact/', views.contact, name='contact'),
    path('change_password/', views.change_password, name='change_password')
]
