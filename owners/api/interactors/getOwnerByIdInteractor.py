from django.http import JsonResponse
from owners.api.models import Owner


def getOwnerByIdInteractor(ownerId):
    try:
        owner = Owner.objects.get(pk=ownerId)
        return owner
    except Exception as e:
        print("error: ", e)
        return JsonResponse({'error': str(e)}, status=500)