from django.http import JsonResponse
from licensePlates.api.models import LicensePlate

def getLicensePlateByIdInteractor(licensePlateId):
    try:
        licensePlate = LicensePlate.objects.get(pk=licensePlateId)
        return licensePlate
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)