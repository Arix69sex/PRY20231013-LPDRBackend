from django.http import JsonResponse
from externalInfractions.api.models import ExternalInfraction

def createMockInfractionInteractor(code, infractionCode, ballotNumber, name, level, fine, date):
    try:
        mockInfractions = ExternalInfraction.objects.create(code=code, infractionCode=infractionCode, ballotNumber=ballotNumber, name= name, level=level, fine=fine, date=date)
        return mockInfractions
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)