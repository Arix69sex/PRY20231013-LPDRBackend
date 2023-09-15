from django.http import JsonResponse

from users.api.interface.JWT import JWT
from functools import wraps
from django.http import JsonResponse
import jwt


def JwtAuthRequired(viewFunction):
    @wraps(viewFunction)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        JWTinstance = JWT()
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]

            payload = JWTinstance.decode(token)

            try:
                payload = JWTinstance.decode(token)
                return viewFunction(request, *args, **kwargs)

            except jwt.ExpiredSignatureError:
                print("payrolad", payload)
                return JsonResponse({'error': 'Token has expired'}, status=401)
            except jwt.DecodeError:
                print("payrolad", payload)
                return JsonResponse({'error': 'Token is invalid'}, status=401)

        return JsonResponse({'error': 'Authentication required'}, status=401)

    return _wrapped_view