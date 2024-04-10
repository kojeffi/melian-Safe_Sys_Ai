# models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50, default='Oil and Gas')

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

class Regulation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    industry = models.CharField(max_length=50, default='Oil and Gas')

class Incident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()

class TrainingModule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    industry = models.CharField(max_length=50, default='Oil and Gas')
