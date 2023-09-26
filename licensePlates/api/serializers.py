from rest_framework import serializers
from licensePlates.api.models import LicensePlate

class LicencePlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensePlate 
        fields = ('id', 'code', 'latitude', 'longitude', 'hasInfractions', 'takenActions', 'user', 'createdAt')

