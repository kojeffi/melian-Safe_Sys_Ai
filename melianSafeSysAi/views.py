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



from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send email
        send_mail(
            subject,
            message,
            email,
            ['omondijeff88@gmail.com'],  # Change this to your email address
            fail_silently=False,
        )
        return JsonResponse({'success': True})

    return render(request, 'index.html')
