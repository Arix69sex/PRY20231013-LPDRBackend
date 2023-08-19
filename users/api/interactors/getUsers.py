from django.http import JsonResponse
from users.api.models import User

def getUsersInteractor():
    try:
        users = User.objects.all()
        return users
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)