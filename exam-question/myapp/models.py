from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    question = models.CharField(max_length=500, primary_key=True)
    date_published = models.DateTimeField()

class PollModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField()