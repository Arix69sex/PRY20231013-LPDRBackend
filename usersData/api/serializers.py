from rest_framework import serializers
from users.api.models import UserData  # Import your User model from the users app

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData  # Specify the model that the serializer is based on
        fields = ('id', 'identification', "names", "lastNames", "address", "phoneNumber")
        # Add any other fields you want to include in your API response

    # You can also define custom validation or additional methods if needed