from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def chatbot_view(request):
    return render(request, 'index.html')
