from licensePlates.api.models import LicensePlate
import io

def createLicensePlateInteractor(user, code, latitude, longitude, hasInfractions, takenActions, imageDataBytes):
    try:
        licensePlate = LicensePlate.objects.create(user=user, code= code, latitude=latitude, longitude=longitude, hasInfractions=hasInfractions, takenActions=takenActions)
        imageData = io.BytesIO(imageDataBytes)
        licensePlate.imageData.save(f'example_licensePlate_${licensePlate.id}.jpg', imageData, save=True)
        return licensePlate
    except Exception as e:
        print("error: ", e)
        return False