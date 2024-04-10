# Generated by Django 5.0.4 on 2024-04-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('severity', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
