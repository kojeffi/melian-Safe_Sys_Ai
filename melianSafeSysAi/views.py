from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


from django.shortcuts import render


def dashboard(request):
    user = request.user
    # Implement dashboard logic here
    return render(request, 'dashboard/index.html', {'user': user})


def profile(request):
    # Retrieve the authenticated user
    user = request.user
    return render(request, 'dashboard/pages-profile.html', {'user': user})


def dashboard(request):
    user = request.user  # Assuming user is authenticated
    return render(request, 'dashboard/index.html', {'user': user})


def about(request):
    return render(request, 'about.html')


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
