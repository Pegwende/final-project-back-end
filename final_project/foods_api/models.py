from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.IntegerField()
