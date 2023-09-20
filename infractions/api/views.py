import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from infractions.api.interactors.createInfractionInteractor import createInfractionInteractor
from infractions.api.interactors.getInfractionByIdInteractor import getInfractionByIdInteractor
from infractions.api.interactors.getInfractionsByLicensePlateInteractor import getInfractionsByLicensePlateInteractor
from infractions.api.interactors.getInfractionsInteractor import getInfractionsInteractor
from infractions.api.interactors.updateInfractionInteractor import updateInfractionInteractor
from licensePlates.api.interactors.getLicensePlateByIdInteractor import getLicensePlateByIdInteractor
from infractions.api.serializers import InfractionSerializer
from users.api.decorators.JwtAuthRequired import JwtAuthRequired

@require_http_methods(["GET"])
def getInfractions(request):
    infractions = getInfractionsInteractor()
    infractionData = [InfractionSerializer(infraction).data for infraction in infractions]
    return JsonResponse({'infractions': infractionData})

@JwtAuthRequired
@require_http_methods(["GET"])
def getInfractionById(request, infractionId):
    infraction = getInfractionByIdInteractor(infractionId)
    if isinstance(infraction, JsonResponse):
        return infraction
    else:
        infraction = InfractionSerializer(infraction)
    return JsonResponse({'infraction': infraction.data})

@JwtAuthRequired
@require_http_methods(["GET"])
def getInfractionByLicensePlateId(request, licensePlateId):
    licensePlate = getLicensePlateByIdInteractor(licensePlateId)
    infractions = getInfractionsByLicensePlateInteractor(licensePlate)
    if isinstance(infractions, JsonResponse):
        return infractions
    elif len(infractions) < 1:
        return JsonResponse({'infraction': []}, status=200, safe=False)
    else:
        infractions = InfractionSerializer(infractions, many=True)
    return JsonResponse({'infraction': infractions.data})

@JwtAuthRequired
@require_http_methods(["POST"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def createInfraction(request):
    body = json.loads(request.body.decode('utf-8'))

    name = body.get("name")
    level = body.get("level")
    fine = body.get("fine")
    licensePlateId = body.get("licensePlateId")
    licensePlate = getLicensePlateByIdInteractor(licensePlateId)
    
    infractionCreated = createInfractionInteractor(licensePlate, name, level, fine)

    if infractionCreated != None:
        statusCode = 201
        responseMessage = 'Infraction created successfully'
    else:
        statusCode = 400
        responseMessage = 'Infraction creation failed'
    return JsonResponse(responseMessage, status=statusCode, safe=False)

@require_http_methods(["PATCH"])
@JwtAuthRequired
@csrf_exempt   # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def updateInfraction(request, infractionId):
    if (request.method == "PATCH"):
        body = json.loads(request.body.decode('utf-8'))

        name = body.get("name")
        level = body.get("level")
        fine = body.get("fine")
        infraction = getInfractionByIdInteractor(infractionId)
        infractionUpdated = updateInfractionInteractor(infraction, name, level, fine)

        if infractionUpdated:
            statusCode = 200
            responseMessage = 'Infraction updated successfully'
        else:
            statusCode = 400
            responseMessage = 'Infraction update failed'
        return JsonResponse(responseMessage, status=statusCode, safe=False)
    else:
        return JsonResponse("Method not allowed", status=405, safe=False)