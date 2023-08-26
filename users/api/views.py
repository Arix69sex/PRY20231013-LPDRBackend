from datetime import datetime, timedelta
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from users.api.decorators.JwtAuthRequired import JwtAuthRequired
from users.api.interactors.createUser import createUserInteractor
from users.api.interactors.getUserByEmail import getUserByEmailInteractor
from users.api.interactors.getUserById import getUserByIdInteractor
from users.api.interactors.getUsers import getUsersInteractor
from users.api.interactors.updateUser import updateUserInteractor
from users.api.interactors.deleteUser import deleteUserInteractor
from users.api.interactors.userExists import userExists
from users.api.interface.Encryptor import Encryptor
from users.api.lib.validateValidEmail import isValidEmail
from users.api.serializers import UserSerializer
from users.api.interface.JWT import JWT
from django.contrib.auth.decorators import login_required

@require_http_methods(["GET"])
def getUsers(request):
    users = getUsersInteractor()
    userData = [UserSerializer(user).data for user in users]
    return JsonResponse({'users': userData})

@JwtAuthRequired
@require_http_methods(["GET"])
def getUsersById(request, userId):
    user = getUserByIdInteractor(userId)
    if isinstance(user, JsonResponse):
        return user
    else:
        userData = UserSerializer(user)
    return JsonResponse({'user': userData.data})

# Deprecated endpoint. Creation of User should only be done via signUp. Stays here for now because is useful for testing
@JwtAuthRequired
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
@JwtAuthRequired
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
@JwtAuthRequired
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
    
@require_http_methods(["POST"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def login(request):
    body = json.loads(request.body.decode('utf-8'))
    
    JWTinstance = JWT()
    encryptorInstance = Encryptor()

    email = body.get("email")
    password = body.get("password")

    user = getUserByEmailInteractor(email)
    if userExists and encryptorInstance.verify(password, user[0].password):
        expirationTime = datetime.utcnow() + timedelta(days=7)
        statusCode = 201
        responseMessage = JWTinstance.encode({
            "id": user[0].id,
            "email": email,
           "exp": expirationTime
        })
    else:
        statusCode = 400
        responseMessage = "User email or password is incorrect."
    return JsonResponse(responseMessage, status=statusCode, safe=False)

@require_http_methods(["POST"])
@csrf_exempt  # Use this decorator for development to disable CSRF protection; use proper CSRF handling in production
def signUp(request):
    body = json.loads(request.body.decode('utf-8'))
    JWTinstance = JWT()
    encryptorInstance = Encryptor()
    email = body.get("email")
    password = body.get("password")
    encryptedPassword = encryptorInstance.encrypt(password)
    if not isValidEmail(email):
        return JsonResponse("User email is not valid.", status=400, safe=False)
    if userExists(email):
        return JsonResponse("User email is not unique.", status=400, safe=False)
    
    userCreated = createUserInteractor(email, encryptedPassword)
    expirationTime = datetime.utcnow() + timedelta(days=7)

    if userCreated:
        statusCode = 201
        responseMessage = JWTinstance.encode({
            "id": userCreated.id,
            "email": email,
            "exp": expirationTime
        })
    else:
        statusCode = 400
        responseMessage = 'User data creation failed'
    return JsonResponse(responseMessage, status=statusCode, safe=False)