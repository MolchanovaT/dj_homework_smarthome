from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
