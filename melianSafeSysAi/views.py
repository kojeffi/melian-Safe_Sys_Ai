from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def acceptable(request):
    return render(request, 'acceptable.html')
def accessibility(request):
    return render(request, 'accessibility.html')
def contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def privacy(request):
    return render(request, 'privacy.html')

def services(request):
    return render(request, 'services.html')

def terms(request):
    return render(request, 'terms.html')