from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import SafetyTrainingResource, Category, UserProgress

@login_required
def training_resources(request):
    categories = Category.objects.all()
    resources = SafetyTrainingResource.objects.all()
    progress, _ = UserProgress.objects.get_or_create(user=request.user)
    completed_resources = progress.completed_resources.all()
    return render(request, 'dashbord/training_resources.html', {'categories': categories, 'resources': resources, 'completed_resources': completed_resources})

@login_required
def resource_detail(request, resource_id):
    resource = get_object_or_404(SafetyTrainingResource, pk=resource_id)
    return render(request, 'dashbord/resource_detail.html', {'resource': resource})

@login_required
def mark_resource_completed(request, resource_id):
    resource = get_object_or_404(SafetyTrainingResource, pk=resource_id)
    progress, _ = UserProgress.objects.get_or_create(user=request.user)
    progress.completed_resources.add(resource)
    progress.save()
    return redirect('training_resources')