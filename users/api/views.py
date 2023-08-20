import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from users.api.interactors.createUser import createUserInteractor
from users.api.interactors.getUserById import getUserByIdInteractor
from users.api.interactors.getUsers import getUsersInteractor
from users.api.interactors.updateUser import updateUserInteractor
from users.api.interactors.deleteUser import deleteUserInteractor
from users.api.interactors.userExists import userExists
from users.api.lib.validateValidEmail import isValidEmail
from users.api.serializers import UserSerializer

@require_http_methods(["GET"])
def getUsers(request):
    users = getUsersInteractor()
    userData = [UserSerializer(user).data for user in users]
    return JsonResponse({'users': userData})

@require_http_methods(["GET"])
def getUsersById(request, userId):
    user = getUserByIdInteractor(userId)
    if isinstance(user, JsonResponse):
        return user
    else:
        userData = UserSerializer(user)
    return JsonResponse({'user': userData.data})

@require_http_methods(["POST"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def createUser(request):
    body = json.loads(request.body.decode('utf-8'))

    email = body.get("email")
    password = body.get("password")
    print("email", email)

    if not isValidEmail(email):
        raise Exception("User email is not valid")
    if userExists(email):
        raise Exception("User email is not unique")
    
    userCreated = createUserInteractor(email, password)

    if userCreated:
        statusCode = 201
        responseMessage = 'User created successfully'
    else:
        statusCode = 400
        responseMessage = 'User creation failed'
    return JsonResponse(responseMessage, status=statusCode, safe=False)

@require_http_methods(["PATCH"])
@csrf_exempt   # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def updateUser(request, userId):
    if (request.method == "PATCH"):
        body = json.loads(request.body.decode('utf-8'))

        email = body.get("email")
        password = body.get("password")
        user = getUserByIdInteractor(userId)
        userUpdated = updateUserInteractor(user, email, password)

        if userUpdated:
            statusCode = 200
            responseMessage = 'User updated successfully'
        else:
            statusCode = 400
            responseMessage = 'User update failed'
        return JsonResponse(responseMessage, status=statusCode, safe=False)
    else:
        return JsonResponse("Method not allowed", status=405, safe=False)
    
@require_http_methods(["DELETE"])
@csrf_exempt # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def deleteUser(request, userId):
    if (request.method == "DELETE"):

        userToDelete = getUserByIdInteractor(userId)
        userDeleted = deleteUserInteractor(userToDelete)

        if userDeleted:
            statusCode = 200
            responseMessage = 'User deleted successfully'
        else:
            statusCode = 400
            responseMessage = 'User delete failed'
        return JsonResponse(responseMessage, status=statusCode, safe=False)
    else:
        return JsonResponse("Method not allowed", status=405, safe=False)