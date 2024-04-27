from django.shortcuts import render
from .models import Message

def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST['user_message']
        # Define your chatbot rules here:
        bot_response = "Sorry, I can't understand."

        # Example rule: Greet the user
        if user_message.lower() == "hello":
            bot_response = "Hi there! How can I help you today?"
        elif user_message.lower() == "how are you?":
            bot_response = "I'm just a bot, but thanks for asking!"
        elif "weather" in user_message.lower():
            bot_response = "I'm not a weather bot, but you can check the weather on weather.com."
        elif "time" in user_message.lower():
            bot_response = "I don't have access to real-time information, but it's probably time for you to take a break!"
        elif "thank you" in user_message.lower() or "thanks" in user_message.lower():
            bot_response = "You're welcome!"
        elif "help" in user_message.lower():
            bot_response = "Sure, I'm here to help. What do you need assistance with?"
        elif "bye" in user_message.lower() or "goodbye" in user_message.lower():
            bot_response = "Goodbye! Feel free to come back anytime."
        elif "recommendation" in user_message.lower():
            bot_response = "Sure! What type of recommendation are you looking for?"
        elif "order" in user_message.lower():
            bot_response = "To place an order, please visit our website or contact customer support."
        elif "news" in user_message.lower():
            bot_response = "You can find the latest news on popular news websites like BBC, CNN, or The New York Times."
        elif "contact" in user_message.lower():
            bot_response = "You can contact us at contact@example.com or call us at +123456789."
        elif "account" in user_message.lower() or "login" in user_message.lower():
            bot_response = "To access your account, please visit our website and log in with your credentials."
        elif "tutorial" in user_message.lower():
            bot_response = "You can find tutorials on various topics on YouTube, Udemy, or Coursera."
        elif "error" in user_message.lower():
            bot_response = "If you're experiencing an error, please provide more details so I can assist you better."
        elif "pricing" in user_message.lower():
            bot_response = "For pricing information, please visit our website or contact our sales team."
        elif "cancel" in user_message.lower() or "refund" in user_message.lower():
            bot_response = "For cancellation or refund requests, please contact our customer support team."
        elif "delivery" in user_message.lower():
            bot_response = "Delivery times may vary depending on your location and shipping method. Please check our website for more information."
        elif "payment" in user_message.lower() or "pay" in user_message.lower():
            bot_response = "You can make payments online through our website using various payment methods."
        elif "feedback" in user_message.lower() or "review" in user_message.lower():
            bot_response = "We appreciate your feedback! You can leave a review on our website or contact us directly."
        elif "password" in user_message.lower():
            bot_response = "If you forgot your password, you can reset it on our website."
        elif "feature" in user_message.lower():
            bot_response = "If you have any feature requests, feel free to share them with us. We're always looking for ways to improve!"
        elif "support" in user_message.lower():
            bot_response = "For technical support, please visit our support page or contact our support team."
        elif "privacy" in user_message.lower() or "policy" in user_message.lower():
            bot_response = "Our privacy policy can be found on our website. We take privacy seriously and ensure that your data is protected."
        elif "partnership" in user_message.lower():
            bot_response = "For partnership inquiries, please email us at partnership@example.com."
        elif "upgrade" in user_message.lower() or "update" in user_message.lower():
            bot_response = "To upgrade or update your account, please log in to your account on our website and follow the instructions."
        elif "event" in user_message.lower():
            bot_response = "For information about upcoming events, please visit our events page or subscribe to our newsletter."
        elif "career" in user_message.lower() or "job" in user_message.lower():
            bot_response = "To view available career opportunities, please visit our careers page on our website."
        elif "discount" in user_message.lower() or "promo" in user_message.lower():
            bot_response = "For discounts or promotions, keep an eye on our website or subscribe to our newsletter for updates."
        elif "feedback" in user_message.lower():
            bot_response = "We value your feedback! Please let us know how we can improve our services."
        elif "chatbot" in user_message.lower():
            bot_response = "Yes, I'm a chatbot here to assist you!"

        # Save the conversation
        message = Message.objects.create(user_message=user_message, bot_response=bot_response)

        return render(request, 'index.html', {'message': message})
    else:
        return render(request, 'index.html', {})
