from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()

class Laptop(models.Model):

    brand=models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100, null=True)