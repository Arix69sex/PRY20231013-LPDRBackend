from rest_framework import serializers
from owners.api.models import Owner  # Import your User model from the users app

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner  # Specify the model that the serializer is based on
        fields = ('id', 'identification', "names", "lastNames", "address", "phoneNumber", "licensePlate")
        # Add any other fields you want to include in your API response

    # You can also define custom validation or additional methods if needed