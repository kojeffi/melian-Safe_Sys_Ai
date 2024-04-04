from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def quote(request):
    return render(request, 'get-a-quote.html')
def pricing(request):
    return render(request, 'pricing.html')
def sample(request):
    return render(request, 'sample-inner-page.html')
def servicedetails(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')