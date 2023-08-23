from rest_framework import serializers
from infractions.api.models import Infraction  # Import your User model from the users app

class InfractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraction  # Specify the model that the serializer is based on
        fields = ('id', 'name', 'level', 'fine', 'licensePlate')
        # Add any other fields you want to include in your API response

    # You can also define custom validation or additional methods if needed