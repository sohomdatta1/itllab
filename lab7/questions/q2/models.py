from django.db import models

# Create your models here.
class Lives(models.Model):
    person_name = models.CharField(max_length=100, primary_key=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Works(models.Model):
    person_name = models.OneToOneField(to=Lives, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    salary = models.IntegerField()