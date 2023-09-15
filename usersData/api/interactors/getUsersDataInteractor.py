from django.http import JsonResponse
from usersData.api.models import UserData

def getUsersDataInteractor():
    try:
        usersData = UserData.objects.all()
        return usersData
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)