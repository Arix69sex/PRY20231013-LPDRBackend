from externalInfractions.api.interactors.getInfractionsByPlateCodeInteractor import getInfractionsByPlateCodeInteractor
from externalInfractions.api.serializers import ExternalInfractionSerializer


def getExternalInfracionsByCode(code):
    externalInfractionsQuerySet = getInfractionsByPlateCodeInteractor(code)
    externalInfractions = [ExternalInfractionSerializer(externalInfraction).data for externalInfraction in externalInfractionsQuerySet]
    return externalInfractions;