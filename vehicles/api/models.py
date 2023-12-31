from django.db import models

from licensePlates.api.models import LicensePlate

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    licensePlate = models.ForeignKey(LicensePlate, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand, self.model, self.year, self.licensePlate