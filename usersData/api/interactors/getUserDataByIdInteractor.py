from django.http import JsonResponse
from usersData.api.models import UserData

def getUserDataByIdInteractor(userDataId):
    try:
        userData = UserData.objects.get(pk=userDataId)
        return userData
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)