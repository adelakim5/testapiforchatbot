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
    q01 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q02 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q03 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q04 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q05 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q06 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q07 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q08 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q09 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q10 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q11 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q12 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES) 
    q13 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q14 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q15 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q16 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q17 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q18 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q19 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    q20 = models.IntegerField(default=Rarely, choices=STATUS_CHOICES)
    total = models.IntegerField(default=0)

     