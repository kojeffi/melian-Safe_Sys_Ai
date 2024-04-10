from rest_framework import viewsets
from .models import AIDrivenSafetyManagement
from .serializers import AIDrivenSafetyManagementSerializer


class AIDrivenSafetyManagementViewSet(viewsets.ModelViewSet):
    queryset = AIDrivenSafetyManagement.objects.all()
    serializer_class = AIDrivenSafetyManagementSerializer


from django.shortcuts import render
from .models import AIDrivenSafetyManagement


def ai_driven_safety_management(request):
    description = AIDrivenSafetyManagement.objects.first().description
    return render(request, 'safety_management/ai_safety_management.html', {'description': description})



from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import AIDrivenSafetyManagement
from .serializers import AIDrivenSafetyManagementSerializer
import json

class AIDrivenSafetyManagementViewSet(viewsets.ModelViewSet):
    queryset = AIDrivenSafetyManagement.objects.all()
    serializer_class = AIDrivenSafetyManagementSerializer

    def get_chart_data(self, request, *args, **kwargs):
        instance = self.get_object()
        chart_data = instance.chart_data
        # Process chart data as needed
        return Response(chart_data)

    def update_data_entry(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.data_entry = request.data.get('data_entry')
        instance.save()
        return Response({'message': 'Data entry updated successfully'})

