from django.http import JsonResponse
from vehicles.api.models import Vehicle

def getVehiclesInteractor():
    try:
        vehicles = Vehicle.objects.all()
        return vehicles
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)