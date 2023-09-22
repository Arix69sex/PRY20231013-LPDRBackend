from infractions.api.interactors.createInfractionInteractor import createInfractionInteractor
from infractions.api.serializers import InfractionSerializer

def createInfractionsOfLicensePlate(licensePlate, externalInfractions):
    infractionsCreated = []
    
    for externalInfraction in externalInfractions:
        name = externalInfraction["name"]
        level = externalInfraction["level"]
        fine = externalInfraction["fine"]
        print("name", name)
        print("level", level)
        print("fine", fine)

        infractionCreated = createInfractionInteractor(licensePlate=licensePlate, name=name, level=level, fine=fine)
        infraction = InfractionSerializer(infractionCreated)
        print("infraction Created", infraction.data)
        infractionsCreated.append(infraction.data)
    
    return infractionsCreated;