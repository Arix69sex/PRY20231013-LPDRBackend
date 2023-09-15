from django.http import JsonResponse
from infractions.api.models import Infraction

def getInfractionsByLicensePlateInteractor(licensePlate):
    try:
        infraction = Infraction.objects.filter(licensePlate=licensePlate)
        return infraction
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)