from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from externalInfractions.api.interactors.getInfractionsByPlateCodeInteractor import getInfractionsByPlateCodeInteractor
from externalInfractions.api.serializers import ExternalInfractionSerializer

@require_http_methods(["GET"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def getMockInfractionsByCode(request, code):
    externalInfractionsQuerySet = getInfractionsByPlateCodeInteractor(code)
    externalInfractions = [ExternalInfractionSerializer(externalInfraction).data for externalInfraction in externalInfractionsQuerySet]
    return JsonResponse({'externalInfractions': externalInfractions})
