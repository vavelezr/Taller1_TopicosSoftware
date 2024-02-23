from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 70)
    desc = models.CharField(max_length = 300)
    price = models.IntegerField()
    category = models.CharField(max_length = 70)
    quantity = models.IntegerField()
    
    