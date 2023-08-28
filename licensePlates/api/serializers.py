from rest_framework import serializers
from licensePlates.api.models import LicensePlate  # Import your User model from the users app

class LicencePlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicensePlate  # Specify the model that the serializer is based on
        fields = ('id', 'code', 'latitude', 'longitude', 'hasInfractions', 'takenActions', 'imageData', 'user')
        # Add any other fields you want to include in your API response

    # You can also define custom validation or additional methods if needed