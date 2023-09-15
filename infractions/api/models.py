from django.db import models

from licensePlates.api.models import LicensePlate

class Infraction(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    fine = models.FloatField()
    licensePlate = models.ForeignKey(LicensePlate, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.level, self.fine, self.licensePlate