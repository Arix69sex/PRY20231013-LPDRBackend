from django.http import JsonResponse
from licensePlates.api.models import LicensePlate

def getLicensePlatesInteractor():
    try:
        licensePlate = LicensePlate.objects.all()
        return licensePlate
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)