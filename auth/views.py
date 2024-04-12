from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You have successfully registered. Please login.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'auth/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Implement login logic here (e.g., authenticate user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'auth/signin.html', {'form': form})

def logout(request):
    return render(request, 'index.html')


def dashboard(request):
    user = request.user  # Assuming user is authenticated
    return render(request, 'dashbord/index.html',{'user': user})

from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CustomUser

@login_required
def profile(request):
    # Retrieve the currently logged-in user
    user = request.user
    return render(request, 'dashboard/pages-profile.html', {'user': user})