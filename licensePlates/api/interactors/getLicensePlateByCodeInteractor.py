from django.http import JsonResponse
from licensePlates.api.models import LicensePlate

def getLicensePlateByCodeInteractor(code):
    try:
        licensePlate = LicensePlate.objects.filter(code=code)
        return licensePlate
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)