from vehicles.api.models import Vehicle

def createVehicleInteractor(licensePlate, brand, model, year):
    try:
        Vehicle.objects.create(licensePlate=licensePlate, model= model, brand=brand, year=year)
        return True
    except Exception as e:
        print("error: ", e)
        return False