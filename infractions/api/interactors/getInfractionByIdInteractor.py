from django.http import JsonResponse
from infractions.api.models import Infraction

def getInfractionByIdInteractor(infractionId):
    try:
        infraction = Infraction.objects.get(pk=infractionId)
        return infraction
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)