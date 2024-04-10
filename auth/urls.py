from django.urls import path
from . import views as my_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', my_views.register, name='register'),
    path('login/', my_views.login, name='login'),
    path('dashboard/', my_views.dashboard, name='dashboard'),
    path('logout/', my_views.logout, name='logout'),
    path('profile/', my_views.profile, name='profile-url'),
]
