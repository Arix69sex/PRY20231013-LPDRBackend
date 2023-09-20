from django.db import models

class ExternalInfraction(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    fine = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code, self.name, self.level, self.fine