from infractions.api.models import Infraction

def createInfractionInteractor(licensePlate, name, level, fine):
    try:
        infraction = Infraction.objects.create(licensePlate=licensePlate, name= name, level=level, fine=fine)
        return infraction
    except Exception as e:
        print("error: ", e)
        return None