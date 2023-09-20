from django.http import JsonResponse
from externalInfractions.api.models import ExternalInfraction

def createMockInfractionInteractor(code, name, level, fine):
    try:
        mockInfractions = ExternalInfraction.objects.create(code=code, name= name, level=level, fine=fine)
        return mockInfractions
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)