def updatelicensePlateInteractor(licensePlateToUpdate, code, latitude, longitude, hasInfractions, takenActions, imageData):
    try:
        if code: licensePlateToUpdate.code = code;
        if latitude: licensePlateToUpdate.latitude = latitude;
        if longitude: licensePlateToUpdate.longitude = longitude;
        if hasInfractions: licensePlateToUpdate.hasInfractions = hasInfractions;
        if takenActions: licensePlateToUpdate.takenActions = takenActions;
        if imageData: licensePlateToUpdate.imageData = imageData;

        licensePlateToUpdate.save()
        return True
    except Exception as e:
        print("error: ", e)
        return False