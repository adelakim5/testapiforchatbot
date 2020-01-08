from django.db import models

# Create your models here.
    
class User(models.Model):
    user = models.CharField(max_length=100, default='')
    
class Post(models.Model):
    question = models.CharField(max_length=50, default='')
    answer = models.IntegerField(default=0)
    userId = models.ForeignKey('User', blank=True, on_delete=models.CASCADE)

     