from licensePlates.api.models import LicensePlate

def createLicensePlateInteractor(user, code, latitude, longitude, hasInfractions, takenActions, imageData):
    try:
        licensePlate = LicensePlate.objects.create(user=user, code= code, latitude=latitude, longitude=longitude, hasInfractions=hasInfractions, takenActions=takenActions, imageData=imageData)
        return licensePlate
    except Exception as e:
        print("error: ", e)
        return False