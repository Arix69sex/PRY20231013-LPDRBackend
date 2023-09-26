from django.db import models
from django.utils import timezone

from licensePlates.api.models import LicensePlate

class Infraction(models.Model):
    name = models.CharField(max_length=100)
    infractionCode = models.TextField(default="M00")
    ballotNumber = models.TextField(default="0")
    level = models.CharField(max_length=100)
    fine = models.FloatField()
    licensePlate = models.ForeignKey(LicensePlate, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.infractionCode, self.ballotNumber, self.level, self.fine, self.licensePlate, self.date