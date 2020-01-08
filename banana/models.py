from django.db import models

# Create your models here.
class Post(models.Model):
    # title = models.CharField(max_length=50)
    # content = models.TextField()
    Rarely = 0
    Seldom = 1
    Often = 2
    Almost = 3
    STATUS_CHOICES = (
        (Rarely, '극히 드물다'),
        (Seldom, '가끔 있었다'),
        (Often, '종종 있었다'),
        (Almost, '대부분 그랬다'),
    )
    
    userId = models.TextField(default='')
    q01 = models.IntegerField(default=Rarely choices=STATUS_CHOICES)
    q02 = models.IntegerField(default=0 choices=Score.choices)
    q03 = models.IntegerField(default=0 choices=Score.choices)
    q04 = models.IntegerField(default=0 choices=Score.choices)
    q05 = models.IntegerField(default=0 choices=Score.choices)
    q06 = models.IntegerField(default=0 choices=Score.choices)
    q07 = models.IntegerField(default=0 choices=Score.choices)
    q08 = models.IntegerField(default=0 choices=Score.choices)
    q09 = models.IntegerField(default=0 choices=Score.choices)
    q10 = models.IntegerField(default=0 choices=Score.choices)
    q11 = models.IntegerField(default=0 choices=Score.choices)
    q12 = models.IntegerField(default=0 choices=Score.choices) 
    q13 = models.IntegerField(default=0 choices=Score.choices)
    q14 = models.IntegerField(default=0 choices=Score.choices)
    q15 = models.IntegerField(default=0 choices=Score.choices)
    q16 = models.IntegerField(default=0 choices=Score.choices)
    q17 = models.IntegerField(default=0 choices=Score.choices)
    q18 = models.IntegerField(default=0 choices=Score.choices)
    q19 = models.IntegerField(default=0 choices=Score.choices)
    q20 = models.IntegerField(default=0 choices=Score.choices)
    total = models.IntegerField(default=0)

     