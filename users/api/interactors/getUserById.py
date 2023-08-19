from requests import Response
from users.api.models import User
from rest_framework import status

def getUserByIdInteractor(userId):
    try:
        # Check if the user exists
        user = User.objects.get(pk=userId)
        return user
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
