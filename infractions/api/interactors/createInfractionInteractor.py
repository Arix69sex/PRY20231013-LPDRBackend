from infractions.api.models import Infraction

def createInfractionInteractor(licensePlate, infractionCode, ballotNumber, name, level, fine, date):
    try:
        infraction = Infraction.objects.create(licensePlate=licensePlate, infractionCode=infractionCode, ballotNumber=ballotNumber, name= name, level=level, fine=fine, date=date)
        return infraction
    except Exception as e:
        print("error: ", e)
        return None