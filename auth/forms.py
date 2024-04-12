from django import forms
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser  # Update to use your custom user model
        fields = ['full_name', 'email', 'password', 'confirm_password']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())