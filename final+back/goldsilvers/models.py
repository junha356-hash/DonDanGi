from django.db import models

class GoldPrice(models.Model):
    date = models.DateField(unique=True)
    price = models.FloatField()

class SilverPrice(models.Model):
    date = models.DateField(unique=True)
    price = models.FloatField()
