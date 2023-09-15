from django.db import models

from licensePlates.api.models import LicensePlate

class Owner(models.Model):
    licensePlate = models.ForeignKey(LicensePlate, on_delete=models.CASCADE)
    identification = models.TextField()
    names = models.CharField(max_length=50)
    lastNames = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.identification, self.names, self.lastNames, self.address, self.phoneNumber