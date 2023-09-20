from django.http import JsonResponse
from externalInfractions.api.models import ExternalInfraction

def getInfractionsByPlateCodeInteractor(code):
    try:
        infractions = ExternalInfraction.objects.filter(code=code)
        return infractions
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)