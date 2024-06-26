from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserProfileForm
from .models import Profile, Message
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Subscription
from django.core.mail import send_mail



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('login-url')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_app/register.html', {'form': form})

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

def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST['user_message']
        bot_response = generate_bot_response(user_message)  # Call a function to generate bot responses
        message = Message.objects.create(user_message=user_message, bot_response=bot_response)

        return render(request, 'index.html', {'message': message})
    else:
        return render(request, 'index.html', {})

def generate_bot_response(user_message):
    if 'hello' in user_message.lower():
        return "Hi there! How can I assist you today?"
    elif 'help' in user_message.lower():
        return "Sure, I'm here to help. What do you need assistance with?"
    elif 'how are you' in user_message.lower():
        return "I'm just a bot, but thanks for asking! How can I assist you?"
    elif 'bye' in user_message.lower():
        return "Goodbye! Feel free to return if you have more questions."
    else:
        return "Sorry, I didn't understand that. Can you please rephrase your question?"



def subscribe(request):
    if request.method == 'POST':
        # Handle form submission
        email = request.POST.get('email')

        # Check if the email already exists in the database
        if not Subscription.objects.filter(email=email).exists():
            # Save the email to the database
            subscription = Subscription(email=email)
            subscription.save()

            # Send email confirmation
            subject = 'Subscription Confirmation'
            message = 'Thank you for subscribing!'
            sender_email = 'omondijeff88@gmail.com'  # Your email address
            recipient_list = [email]
            send_mail(subject, message, sender_email, recipient_list)

            # Render the subscription form with a success message
            return render(request, 'index.html', {'success_message': 'Thank you for subscribing!'})
        else:
            # Email already exists, render the form with an error message
            return render(request, 'index.html', {'error_message': 'Email already subscribed!'})
    else:
        # If the request method is GET, render the subscription form
        return render(request, 'index.html')