from datetime import datetime
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from externalInfractions.api.interactors.createMockInfractionInteractor import createMockInfractionInteractor
from externalInfractions.api.serializers import ExternalInfractionSerializer

@require_http_methods(["POST"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def createMockInfraction(request):
    body = json.loads(request.body.decode('utf-8'))

    code = body.get("code")
    infractionCode = body.get("infractionCode")
    ballotNumber = body.get("ballotNumber")
    name = body.get("name")
    level = body.get("level")
    fine = body.get("fine")
    date = body.get("date")
    formatted_date = datetime.strptime(date, '%Y-%m-%d')

    mockInfractionCreated = createMockInfractionInteractor(code, infractionCode, ballotNumber, name, level, fine, formatted_date)
    if mockInfractionCreated:
        statusCode = 201
        mockInfraction = ExternalInfractionSerializer(mockInfractionCreated)
        responseMessage = 'License Plate created successfully'
        response = {
            "responseMessage": responseMessage,
            "mockInfraction": mockInfraction.data
        }
        return JsonResponse(response, status=statusCode, safe=False)
    else:
        statusCode = 400
        responseMessage = 'License Plate creation failed'
        response = {
            "responseMessage": responseMessage,
            "mockInfraction": None,
        }
        return JsonResponse(response, status=statusCode, safe=False)