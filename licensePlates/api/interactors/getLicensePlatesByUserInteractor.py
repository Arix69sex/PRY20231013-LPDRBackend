from django.http import JsonResponse
from licensePlates.api.models import LicensePlate

def getLicensePlatesByUserInteractor(user):
    try:
        licensePlate = LicensePlate.objects.filter(user=user)
        return licensePlate
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)