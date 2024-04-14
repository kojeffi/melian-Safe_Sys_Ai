from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard-url')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_app/register.html', {'form': form})

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
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'user_app/profile.html', {'form': form})


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
