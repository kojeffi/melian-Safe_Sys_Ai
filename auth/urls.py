from django.urls import path
from . import views as my_views

urlpatterns = [
    path('register/', my_views.register, name='register'),
    path('login/', my_views.login, name='login'),
    path('dashboard/', my_views.dashboard, name='dashboard'),
    path('logout/', my_views.logout, name='logout'),
    path('contact/', my_views.contact, name='contact'),
    path('password-reset/', my_views.password_reset, name='password_reset'),
]