from rest_framework import serializers
from .models import AIDrivenSafetyManagement

class AIDrivenSafetyManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIDrivenSafetyManagement
        fields = '__all__'