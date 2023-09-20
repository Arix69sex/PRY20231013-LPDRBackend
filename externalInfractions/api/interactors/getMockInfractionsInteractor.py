from django.http import JsonResponse
from externalInfractions.api.models import ExternalInfraction

def getMockInfractionsInteractor():
    try:
        infractions = ExternalInfraction.objects.all()
        return infractions
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)