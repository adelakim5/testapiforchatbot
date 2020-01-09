from django.db import models

# Create your models here.
    
class User(models.Model):
    user = models.CharField(max_length=100)
    
class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.IntegerField(default=0)
    userId = models.ForeignKey('User', blank=True, on_delete=models.CASCADE)

     