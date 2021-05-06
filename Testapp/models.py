from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=54)
    date=models.DateField()
    hero=models.CharField(max_length=34)
    heroine=models.CharField(max_length=34)
    ratings=models.IntegerField()
