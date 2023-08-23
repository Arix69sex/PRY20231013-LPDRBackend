from django.http import JsonResponse
from owners.api.models import Owner

def getOwnersInteractor():
    try:
        owners = Owner.objects.all()
        return owners
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)