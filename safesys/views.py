# views.py
from django.shortcuts import render
from .models import Company, Employee, Equipment, Regulation, Incident, TrainingModule

def dashboard(request):
    companies = Company.objects.all()
    employees = Employee.objects.all()
    equipments = Equipment.objects.all()
    regulations = Regulation.objects.all()
    incidents = Incident.objects.all()
    training_modules = TrainingModule.objects.all()

    context = {
        'companies': companies,
        'employees': employees,
        'equipments': equipments,
        'regulations': regulations,
        'incidents': incidents,
        'training_modules': training_modules,
    }

    return render(request, 'safesys/realtime.html', context)



