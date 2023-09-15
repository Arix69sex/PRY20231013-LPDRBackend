def updateVehicleInteractor(vehicleToUpdate, model, brand, year):
    try:
        if model: vehicleToUpdate.model = model;
        if brand: vehicleToUpdate.brand = brand;
        if year: vehicleToUpdate.year = year;

        vehicleToUpdate.save()
        return True
    except Exception as e:
        print("error: ", e)
        return False