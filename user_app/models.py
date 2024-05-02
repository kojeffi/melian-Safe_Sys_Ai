from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='static/profile_photos/', blank=True, null=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

@receiver(models.signals.post_save, sender=Profile)
def resize_profile_photo(sender, instance, created, **kwargs):
    if instance.profile_photo:
        img = Image.open(instance.profile_photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(instance.profile_photo.path)


from django.db import models

class Message(models.Model):
    user_message = models.CharField(max_length=200)
    bot_response = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_message} - {self.bot_response}"
