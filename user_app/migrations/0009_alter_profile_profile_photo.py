# Generated by Django 5.0.4 on 2024-05-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0008_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
    ]
