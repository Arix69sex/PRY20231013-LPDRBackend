from django.utils import timezone
from django.db import models

class ExternalInfraction(models.Model):
    code = models.TextField()
    infractionCode = models.TextField(default="M00")
    ballotNumber = models.TextField(default="0")
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    fine = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code, self.infractionCode, self.ballotNumber ,self.name, self.level, self.fine, self.date