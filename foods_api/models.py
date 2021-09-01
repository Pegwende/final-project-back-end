from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    price = models.IntegerField()
    number = models.IntegerField()
    category = models.CharField(max_length=32)
