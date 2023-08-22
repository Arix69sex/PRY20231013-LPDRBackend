from licensePlates.api.models import LicensePlate

def createLicensePlateInteractor(user, code, latitude, longitude, hasInfractions, takenActions):
    try:
        LicensePlate.objects.create(user=user, code= code, latitude=latitude, longitude=longitude, hasInfractions=hasInfractions, takenActions=takenActions)
        return True
    except Exception as e:
        print("error: ", e)
        return False