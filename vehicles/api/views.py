import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from licensePlates.api.interactors.getLicensePlateByIdInteractor import getLicensePlateByIdInteractor
from users.api.decorators.JwtAuthRequired import JwtAuthRequired
from vehicles.api.interactors.createVehicleInteractor import createVehicleInteractor
from vehicles.api.interactors.getVehicleByIdInteractor import getVehicleByIdInteractor
from vehicles.api.interactors.getVehicleByLicensePlateInteractor import getVehicleByLicensePlateInteractor
from vehicles.api.interactors.getVehiclesInteractor import getVehiclesInteractor
from vehicles.api.interactors.updateVehicleInteractor import updateVehicleInteractor
from vehicles.api.lib.validateVehicleHasLicensePlate import validateVehicleHasLicensePlate

from vehicles.api.serializers import VehicleSerializer

@JwtAuthRequired
@require_http_methods(["GET"])
def getVehicles(request):
    vehicles = getVehiclesInteractor()
    vehicles = [VehicleSerializer(vehicle).data for vehicle in vehicles]
    return JsonResponse({'vehicles': vehicles})

@JwtAuthRequired
@require_http_methods(["GET"])
def getVehicleById(request, vehicleId):
    vehicle = getVehicleByIdInteractor(vehicleId)
    if isinstance(vehicle, JsonResponse):
        return vehicle
    else:
        vehicle = VehicleSerializer(vehicle)
    return JsonResponse({'vehicle': vehicle.data})

@JwtAuthRequired
@require_http_methods(["GET"])
def getVehicleByLicensePlateId(request, licensePlateId):
    licensePlate = getLicensePlateByIdInteractor(licensePlateId)
    vehicle = getVehicleByLicensePlateInteractor(licensePlate)
    if isinstance(vehicle, JsonResponse) or not vehicle.exists():
        return JsonResponse({'vehicle': []}, status=200, safe=False)
    else:
        vehicle = VehicleSerializer(vehicle.first())
    return JsonResponse({'vehicle': vehicle.data})

@JwtAuthRequired
@require_http_methods(["POST"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def createVehicle(request):
    body = json.loads(request.body.decode('utf-8'))

    brand = body.get("brand")
    model = body.get("model")
    year = body.get("year")
    licensePlateId = body.get("licensePlateId")
    licensePlate = getLicensePlateByIdInteractor(licensePlateId)
    validateVehicleHasLicensePlate(licensePlate)
    VehicleCreated = createVehicleInteractor(licensePlate, brand, model, year)

    if VehicleCreated:
        statusCode = 201
        responseMessage = 'Vehicle created successfully'
    else:
        statusCode = 400
        responseMessage = 'Vehicle creation failed'
    return JsonResponse(responseMessage, status=statusCode, safe=False)

@require_http_methods(["PATCH"])
@csrf_exempt   # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def updateVehicle(request, vehicleId):
    if (request.method == "PATCH"):
        body = json.loads(request.body.decode('utf-8'))

        brand = body.get("brand")
        model = body.get("model")
        year = body.get("year")

        vehicle = getVehicleByIdInteractor(vehicleId)
        vehicleUpdated = updateVehicleInteractor(vehicle, model, brand, year)

        if vehicleUpdated:
            statusCode = 200
            responseMessage = 'Vehicle updated successfully'
        else:
            statusCode = 400
            responseMessage = 'Vehicle update failed'
        return JsonResponse(responseMessage, status=statusCode, safe=False)
    else:
        return JsonResponse("Method not allowed", status=405, safe=False)