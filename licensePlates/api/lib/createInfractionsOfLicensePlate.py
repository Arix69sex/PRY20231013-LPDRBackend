from infractions.api.interactors.createInfractionInteractor import createInfractionInteractor
from infractions.api.serializers import InfractionSerializer

def createInfractionsOfLicensePlate(licensePlate, externalInfractions):
    infractionsCreated = []
    
    for externalInfraction in externalInfractions:
        name = externalInfraction["name"]
        infractionCode = externalInfraction["infractionCode"]
        ballotNumber = externalInfraction["ballotNumber"]
        level = externalInfraction["level"]
        fine = externalInfraction["fine"]
        date = externalInfraction["date"]
        print("name", name)
        print("level", level)
        print("fine", fine)

        infractionCreated = createInfractionInteractor(licensePlate=licensePlate, infractionCode=infractionCode, ballotNumber=ballotNumber, name=name, level=level, fine=fine, date=date)
        infraction = InfractionSerializer(infractionCreated)
        infractionsCreated.append(infraction.data)
    
    return infractionsCreated;