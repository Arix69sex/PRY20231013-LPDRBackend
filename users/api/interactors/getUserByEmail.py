from django.http import JsonResponse
from users.api.models import User

def getUserByEmailInteractor(email):
    try:
        userData = User.objects.filter(email=email)
        return userData
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)