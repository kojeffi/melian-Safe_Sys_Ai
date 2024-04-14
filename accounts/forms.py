from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'email', 'profile_photo', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }
