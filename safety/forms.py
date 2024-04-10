# safety/forms.py

from django import forms
from .models import AIModel


class TrainModelForm(forms.ModelForm):
    class Meta:
        model = AIModel
        fields = ['name', 'description']  # Add other fields if needed
