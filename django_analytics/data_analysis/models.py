from django.db import models

class Cars(models.Model):
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.FloatField()
    transmission = models.CharField(max_length=255)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=255)
    tax = models.FloatField()
    mpg = models.FloatField()
    engine_size = models.FloatField()
    make = models.CharField(max_length=255)
