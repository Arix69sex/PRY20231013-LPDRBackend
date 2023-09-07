from django.db import models

from users.api.models import User

# Create your models here.
class LicensePlate(models.Model):
    code = models.CharField(max_length=6)
    latitude = models.FloatField()
    longitude = models.FloatField()
    hasInfractions = models.BooleanField(default=False)
    takenActions = models.BooleanField(default=False)
    imageData = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code, self.latitude, self.longitude, self.hasInfractions, self.takenActions, self.user
    

class TestImage(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image