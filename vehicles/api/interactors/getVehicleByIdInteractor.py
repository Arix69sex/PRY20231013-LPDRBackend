from django.http import JsonResponse
from vehicles.api.models import Vehicle


def getVehicleByIdInteractor(vehicleId):
    try:
        vehicle = Vehicle.objects.get(pk=vehicleId)
        return vehicle
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)