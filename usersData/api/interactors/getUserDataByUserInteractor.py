from django.http import JsonResponse
from usersData.api.models import UserData
from django.core.exceptions import ObjectDoesNotExist

def getUserDataByUserInteractor(user):
    try:
        userData = UserData.objects.filter(user=user)
        return userData
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)