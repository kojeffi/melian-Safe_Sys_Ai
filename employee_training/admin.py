# employee_training/admin.py
from django.contrib import admin
from .models import Category, SafetyTrainingResource, UserProgress

admin.site.register(Category)
admin.site.register(SafetyTrainingResource)
admin.site.register(UserProgress)
