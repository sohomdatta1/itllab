from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    price = models.IntegerField()
    description = models.CharField(max_length=5000)