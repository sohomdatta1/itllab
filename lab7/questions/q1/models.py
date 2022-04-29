from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    num_of_visits = models.IntegerField()
    num_of_likes = models.IntegerField()

class Page(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    url = models.URLField()
    views = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)














