from rest_framework import serializers
from vehicles.api.models import Vehicle  # Import your User model from the users app

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle  # Specify the model that the serializer is based on
        fields = ('id', 'brand', 'model', 'year')
        # Add any other fields you want to include in your API response

    # You can also define custom validation or additional methods if needed