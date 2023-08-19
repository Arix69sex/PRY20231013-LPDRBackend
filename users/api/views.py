import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from users.api.interactors.createUser import createUserInteractor
from users.api.interactors.getUserById import getUserByIdInteractor
from users.api.interactors.getUsers import getUsersInteractor
from users.api.interactors.updateUser import updateUserInteractor
from users.api.interactors.deleteUser import deleteUserInteractor
from users.api.serializers import UserSerializer
from django.utils.decorators import method_decorator
from rest_framework.decorators import permission_classes

@require_http_methods(["GET"])
def getUsers(request):
    users = getUsersInteractor()
    userData = [UserSerializer(user).data for user in users]
    return JsonResponse({'users': userData})

@require_http_methods(["GET"])
def getUsersById(request, userId):
    user = getUserByIdInteractor(userId)
    userData = UserSerializer(user)
    return JsonResponse({'user': userData.data})

@require_http_methods(["POST"])  # Ensure that the view only accepts POST requests
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def createUser(request):
    body = json.loads(request.body.decode('utf-8'))

    email = body.get("email")
    password = body.get("password")

    userCreated = createUserInteractor(email, password)

    if userCreated:
        statusCode = 201
        responseMessage = 'User created successfully'
    else:
        statusCode = 400
        responseMessage = 'User creation failed'
    return JsonResponse(responseMessage, status=statusCode)

@require_http_methods(["PATCH"]) # Ensure that the view only accepts PATCH requests
@method_decorator(csrf_exempt)   # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def updateUser(request):
    if (request.method == "PATCH"):
        body = json.loads(request.body.decode('utf-8'))

        id = body.get("id")
        email = body.get("email")
        password = body.get("password")

        userUpdated = updateUserInteractor(id, email, password)

        if userUpdated:
            statusCode = 200
            responseMessage = 'User updated successfully'
        else:
            statusCode = 400
            responseMessage = 'User update failed'
        return JsonResponse(responseMessage, status=statusCode)
    else:
        return JsonResponse("Method not allowed", status=405)
    
@require_http_methods(["DELETE"]) # Ensure that the view only accepts PATCH requests
@method_decorator(csrf_exempt)   # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def deleteUser(request):
    if (request.method == "DELETE"):
        body = json.loads(request.body.decode('utf-8'))

        id = body.get("id")

        userDeleted = deleteUserInteractor(id)

        if userDeleted:
            statusCode = 200
            responseMessage = 'User deleted successfully'
        else:
            statusCode = 400
            responseMessage = 'User delete failed'
        return JsonResponse(responseMessage, status=statusCode)
    else:
        return JsonResponse("Method not allowed", status=405)