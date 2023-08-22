import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from users.api.decorators.JwtAuthRequired import JwtAuthRequired
from users.api.interactors.getUserById import getUserByIdInteractor
from usersData.api.interactors.createUserDataInteractor import createUserDataByIdInteractor
from usersData.api.interactors.getUserDataByIdInteractor import getUserDataByIdInteractor
from usersData.api.interactors.getUserDataByUserInteractor import getUserDataByUserInteractor
from usersData.api.interactors.getUsersDataInteractor import getUsersDataInteractor
from usersData.api.interactors.updateUserDataInteractor import updateUserDataInteractor
from usersData.api.lib.validateUserHasData import validateUserHasData

from usersData.api.serializers import UserDataSerializer

@JwtAuthRequired
@require_http_methods(["GET"])
def getUsersData(request):
    usersData = getUsersDataInteractor()
    usersData = [UserDataSerializer(userData).data for userData in usersData]
    return JsonResponse({'usersData': usersData})

@JwtAuthRequired
@require_http_methods(["GET"])
def getUserDataById(request, userDataId):
    userData = getUserDataByIdInteractor(userDataId)
    if isinstance(userData, JsonResponse):
        return userData
    else:
        userData = UserDataSerializer(userData)
    return JsonResponse({'userData': userData.data})

@JwtAuthRequired
@require_http_methods(["GET"])
def getUserDataByUserId(request, userId):
    user = getUserByIdInteractor(userId)
    userData = getUserDataByUserInteractor(user)
    if isinstance(userData, JsonResponse) or not userData.exists():
        return JsonResponse("User doesn't have User Data", status=400, safe=False)
    else:
        userData = UserDataSerializer(userData.first())
    return JsonResponse({'userData': userData.data})

@JwtAuthRequired
@require_http_methods(["POST"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def createUserData(request, userId):
    body = json.loads(request.body.decode('utf-8'))

    identification = body.get("identification")
    names = body.get("names")
    lastNames = body.get("lastNames")
    address = body.get("address")
    phoneNumber = body.get("lastNames")

    user = getUserByIdInteractor(userId)
    validateUserHasData(user)
    userCreated = createUserDataByIdInteractor(user, identification, names, lastNames, address, phoneNumber)

    if userCreated:
        statusCode = 201
        responseMessage = 'User data created successfully'
    else:
        statusCode = 400
        responseMessage = 'User data creation failed'
    return JsonResponse(responseMessage, status=statusCode, safe=False)

@require_http_methods(["PATCH"])
@csrf_exempt   # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def updateUserData(request, userDataId):
    if (request.method == "PATCH"):
        body = json.loads(request.body.decode('utf-8'))

        identification = body.get("identification")
        names = body.get("names")
        lastNames = body.get("lastNames")
        address = body.get("address")
        phoneNumber = body.get("lastNames")

        userData = getUserDataByIdInteractor(userDataId)
        userDataUpdated = updateUserDataInteractor(userData, identification, names, lastNames, address, phoneNumber)

        if userDataUpdated:
            statusCode = 200
            responseMessage = 'User data updated successfully'
        else:
            statusCode = 400
            responseMessage = 'User data update failed'
        return JsonResponse(responseMessage, status=statusCode, safe=False)
    else:
        return JsonResponse("Method not allowed", status=405, safe=False)