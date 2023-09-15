from vehicles.api.interactors.getVehicleByLicensePlateInteractor import getVehicleByLicensePlateInteractor


def validateVehicleHasLicensePlate(licensePlate):
    hasVehicle = getVehicleByLicensePlateInteractor(licensePlate)
    if hasVehicle.exists():
        raise Exception("License plate already has vehicle")