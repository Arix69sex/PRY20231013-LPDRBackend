from infractions.api.models import Infraction

def createInfractionInteractor(licensePlate, name, level, fine):
    try:
        Infraction.objects.create(licensePlate=licensePlate, name= name, level=level, fine=fine)
        return True
    except Exception as e:
        print("error: ", e)
        return False