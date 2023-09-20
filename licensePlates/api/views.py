import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from infractions.api.serializers import InfractionSerializer
from licensePlates.api.interactors.createLicensePlateInteractor import createLicensePlateInteractor
from licensePlates.api.interactors.getLicensePlateByIdInteractor import getLicensePlateByIdInteractor
from licensePlates.api.interactors.getLicensePlatesByUserInteractor import getLicensePlatesByUserInteractor
from licensePlates.api.interactors.getLicensePlatesInteractor import getLicensePlatesInteractor
from licensePlates.api.interactors.updateLicensePlateInteractor import updatelicensePlateInteractor
from licensePlates.api.interactors.getLicensePlateByCodeInteractor import getLicensePlateByCodeInteractor
from licensePlates.api.lib.checkIfCodeHasInfractions import getExternalInfracionsByCode
from licensePlates.api.models import TestImage
from users.api.decorators.JwtAuthRequired import JwtAuthRequired
from users.api.interactors.getUserById import getUserByIdInteractor
from licensePlates.api.serializers import LicencePlateSerializer
from licensePlates.api.lib.createInfractionsOfLicensePlate import createInfractionsOfLicensePlate

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from lpdr.lpdr import get_license_plate
import cv2
import numpy as np

@require_http_methods(["GET"])
def getLicensePlates(request):
    licensePlates = getLicensePlatesInteractor()
    licensePlateData = [LicencePlateSerializer(licensePlate).data for licensePlate in licensePlates]
    
    return JsonResponse({'licensePlates': licensePlateData})

@JwtAuthRequired
@require_http_methods(["GET"])
def getLicensePlateById(request, licensePlateId):
    licensePlate = getLicensePlateByIdInteractor(licensePlateId)
    if isinstance(licensePlate, JsonResponse):
        return licensePlate
    else:
        licensePlate = LicencePlateSerializer(licensePlate)
    return JsonResponse({'licensePlate': licensePlate.data})

@JwtAuthRequired
@require_http_methods(["GET"])
def getLicensePlateByUserId(request, userId):
    user = getUserByIdInteractor(userId)
    licensePlates = getLicensePlatesByUserInteractor(user)
    print("isinstance(licensePlates, JsonResponse) or len(licensePlates) < 1", isinstance(licensePlates, JsonResponse) or len(licensePlates) < 1)
    if isinstance(licensePlates, JsonResponse):
        return licensePlates
    elif len(licensePlates) < 1:
        return JsonResponse({'licensePlate': []}, status=200, safe=False)
    else:
        licensePlates = LicencePlateSerializer(licensePlates, many=True)
    return JsonResponse({'licensePlate': licensePlates.data})

@JwtAuthRequired
@require_http_methods(["POST"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def createLicensePlate(request):
    body = json.loads(request.body.decode('utf-8'))

    code = body.get("code")
    latitude = body.get("latitude")
    longitude = body.get("longitude")
    hasInfractions = body.get("hasInfractions")
    takenActions = body.get("takenActions")
    userId = body.get("userId")
    imageData = body.get("imageData")
    user = getUserByIdInteractor(userId)
    
    licensePlateCreated = createLicensePlateInteractor(user, code, latitude, longitude, hasInfractions, takenActions, imageData)

    if licensePlateCreated:
        statusCode = 201
        responseMessage = 'License Plate created successfully'
    else:
        statusCode = 400
        responseMessage = 'License Plate creation failed'
    return JsonResponse(responseMessage, status=statusCode, safe=False)

@require_http_methods(["PATCH"])
@JwtAuthRequired
@csrf_exempt   # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def updateLicensePlate(request, licensePlateId):
    if (request.method == "PATCH"):
        body = json.loads(request.body.decode('utf-8'))

        code = body.get("code")
        latitude = body.get("latitude")
        longitude = body.get("longitude")
        hasInfractions = body.get("hasInfractions")
        takenActions = body.get("takenActions")
        imageData = body.get("imageData")
        licensePlate = getLicensePlateByIdInteractor(licensePlateId)

        licensePlateUpdated = updatelicensePlateInteractor(licensePlate, code, latitude, longitude, hasInfractions, takenActions, imageData)
        if licensePlateUpdated:
            statusCode = 200
            responseMessage = 'License plate updated successfully'
        else:
            statusCode = 400
            responseMessage = 'License plate update failed'
        return JsonResponse(responseMessage, status=statusCode, safe=False)
    else:
        return JsonResponse("Method not allowed", status=405, safe=False)
    

@require_http_methods(["POST"])
def detectLicensePlateWithInfractions(request):
    
    body = json.loads(request.body.decode('utf-8'))
    latitude = body.get("latitude")
    longitude = body.get("longitude")
    userId = body.get("userId")
    user = getUserByIdInteractor(userId)
    #img = body.get("image")
    #image = bytes(img)
    im = cv2.imread('/workspace/lpdr/vehicle.jpeg')
    licensePlateTextResult = get_license_plate(im)
    detectedData = []

    for element in licensePlateTextResult:
        elementLen = len(element)
        dataObject = {
            "text": element[elementLen-1],
            "image": element[elementLen-2],
            "type": element[elementLen-3]
        }
        detectedData.append(dataObject)

    licensePlatesCreated = []
    infractionsCreated = []
    for element in detectedData:
        if (element["type"] == "car-plate"):
            foundExistingPlate = getLicensePlateByCodeInteractor(element["text"])
            if len(foundExistingPlate) < 10000:
                infractions = getExternalInfracionsByCode(element["text"])
                if len(infractions) > 0:
                    licensePlateCreated = createLicensePlateInteractor(user, element["text"], latitude, longitude, False, False, element["image"])
                    licensePlatesCreated.append(licensePlateCreated)

                    licensePlatesQuerySet = createInfractionsOfLicensePlate(licensePlateCreated, infractions)
                    infractionsCreated = infractionsCreated + licensePlatesQuerySet

    licensePlateData = [LicencePlateSerializer(licensePlate).data for licensePlate in licensePlatesCreated]

    statusCode = 200

    if len(licensePlateData) > 0:
        statusCode = 201
    response = {
        "licensePlatesCreated": licensePlateData,
        "infractionsCreated": infractionsCreated
    }

    return JsonResponse(response, status=statusCode, safe=False)