from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


from django.shortcuts import render


def dashboard(request):
    user = request.user
    # Implement dashboard logic here
    return render(request, 'dashbord/index.html', {'user': user})


def profile(request):
    # Retrieve the authenticated user
    user = request.user
    return render(request, 'dashbord/index.html', {'user': user})


def dashboard(request):
    user = request.user  # Assuming user is authenticated
    return render(request, 'dashbord/index.html', {'user': user})


