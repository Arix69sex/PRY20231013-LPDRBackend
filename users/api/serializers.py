from rest_framework import serializers
from users.api.models import User  # Import your User model from the users app

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specify the model that the serializer is based on
        fields = ('id', 'email')
        # Add any other fields you want to include in your API response

    # You can also define custom validation or additional methods if needed