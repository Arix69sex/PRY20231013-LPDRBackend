from django.http import JsonResponse
from vehicles.api.models import Vehicle

def getVehicleByLicensePlateInteractor(licensePlate):
    try:
        licensePlate = Vehicle.objects.filter(licensePlate=licensePlate)
        return licensePlate
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)