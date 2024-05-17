
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='static/assets1/img/profile_photos/', blank=True, null=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.profile_photo:
            img = Image.open(self.profile_photo.path)
            if img.height > 462 or img.width > 340:
                output_size = (462, 340)
                img.thumbnail(output_size)
                img.save(self.profile_photo.path)

class Message(models.Model):
    user_message = models.CharField(max_length=200)
    bot_response = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_message} - {self.bot_response}"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
