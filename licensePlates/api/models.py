from django.db import models

from users.api.models import User

# Create your models here.
class LicensePlate(models.Model):
    code = models.CharField(max_length=6)
    latitude = models.FloatField()
    longitude = models.FloatField()
    hasInfractions = models.BooleanField(default=False)
    takenActions = models.BooleanField(default=False)
    imageData = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Code: {self.code}, Latitude: {self.latitude}, Longitude: {self.longitude}, User: {self.user.username}"
    

class TestImage(models.Model):
    image = models.ImageField(upload_to='images/')