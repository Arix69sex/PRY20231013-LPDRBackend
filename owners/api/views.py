import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from licensePlates.api.interactors.getLicensePlateByIdInteractor import getLicensePlateByIdInteractor
from users.api.decorators.JwtAuthRequired import JwtAuthRequired
from owners.api.interactors.createOwnerInteractor import createOwnerInteractor
from owners.api.interactors.getOwnerByIdInteractor import getOwnerByIdInteractor
from owners.api.interactors.getOwnerByLicensePlateInteractor import getOwnerByLicensePlateInteractor
from owners.api.interactors.getOwnersInteractor import getOwnersInteractor
from owners.api.interactors.updateOwnerInteractor import updateOwnerInteractor
from owners.api.lib.validateOwnerHasLicensePlate import validateOwnerHasLicensePlate

from owners.api.serializers import OwnerSerializer

@JwtAuthRequired
@require_http_methods(["GET"])
def getOwners(request):
    owners = getOwnersInteractor()
    owners = [OwnerSerializer(owner).data for owner in owners]
    return JsonResponse({'owners': owners})

@JwtAuthRequired
@require_http_methods(["GET"])
def getOwnerById(request, ownerId):
    owner = getOwnerByIdInteractor(ownerId)
    if isinstance(owner, JsonResponse):
        return owner
    else:
        owner = OwnerSerializer(owner)
    return JsonResponse({'owner': owner.data})

@JwtAuthRequired
@require_http_methods(["GET"])
def getOwnerByLicensePlateId(request, licensePlateId):
    licensePlate = getLicensePlateByIdInteractor(licensePlateId)
    owner = getOwnerByLicensePlateInteractor(licensePlate)
    if isinstance(owner, JsonResponse) or not owner.exists():
        return JsonResponse({'owner': []}, status=200, safe=False)
    else:
        owner = OwnerSerializer(owner.first())
    return JsonResponse({'owner': owner.data})

@JwtAuthRequired
@require_http_methods(["POST"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def createOwner(request):
    body = json.loads(request.body.decode('utf-8'))

    identification = body.get("identification")
    names = body.get("names")
    lastNames = body.get("lastNames")
    address = body.get("address")
    phoneNumber = body.get("lastNames")
    licensePlateId = body.get("licensePlateId")
    licensePlate = getLicensePlateByIdInteractor(licensePlateId)
    validateOwnerHasLicensePlate(licensePlate)
    OwnerCreated = createOwnerInteractor(licensePlate, identification, names, lastNames, address, phoneNumber)

    if OwnerCreated:
        statusCode = 201
        responseMessage = 'Owner created successfully'
    else:
        statusCode = 400
        responseMessage = 'Owner creation failed'
    return JsonResponse(responseMessage, status=statusCode, safe=False)

@require_http_methods(["PATCH"])
@csrf_exempt   # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def updateOwner(request, ownerId):
    if (request.method == "PATCH"):
        body = json.loads(request.body.decode('utf-8'))

        identification = body.get("identification")
        names = body.get("names")
        lastNames = body.get("lastNames")
        address = body.get("address")
        phoneNumber = body.get("lastNames")

        owner = getOwnerByIdInteractor(ownerId)
        ownerUpdated = updateOwnerInteractor(owner,  identification, names, lastNames, address, phoneNumber)

        if ownerUpdated:
            statusCode = 200
            responseMessage = 'Owner updated successfully'
        else:
            statusCode = 400
            responseMessage = 'Owner update failed'
        return JsonResponse(responseMessage, status=statusCode, safe=False)
    else:
        return JsonResponse("Method not allowed", status=405, safe=False)