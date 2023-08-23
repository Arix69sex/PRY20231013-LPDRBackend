from django.http import JsonResponse
from owners.api.models import Owner

def getOwnerByLicensePlateInteractor(licensePlate):
    try:
        owner = Owner.objects.filter(licensePlate=licensePlate)
        return owner
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)