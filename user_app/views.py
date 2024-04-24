# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserProfileForm
from .forms import UserProfileForm
from .models import Profile

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login-url')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_app/register.html', {'form': form})

@login_required
def dashboard(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'dashbord/index.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    username = user.username
    email = user.email
    return render(request, 'dashbord/index.html', {'username': username, 'email': email})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile-url')
    else:
        form = UserProfileForm()
    return render(request, 'dashbord/index.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard-url')
        else:
            return render(request, 'user_app/login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'user_app/login.html')

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashbord/index.html', {'user': user})

@login_required
def profile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-url')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'dashbord/overview.html', {'form': form})



from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse


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
