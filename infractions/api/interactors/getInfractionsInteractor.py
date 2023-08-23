from django.http import JsonResponse
from infractions.api.models import Infraction

def getInfractionsInteractor():
    try:
        infractions = Infraction.objects.all()
        return infractions
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)